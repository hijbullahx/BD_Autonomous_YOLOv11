import os
import xml.etree.ElementTree as ET
from tqdm import tqdm

# PATHS
XML_DIR = "data/processed/xml_raw"
OUTPUT_DIR = "data/processed/labels"

# CRITICAL: This mapping must match data/bd_traffic.yaml EXACTLY
# I have inspected the raw dataset class names and mapped them to our thesis IDs.
CLASS_MAP = {
    "car": 0, "Car": 0,
    "bus": 1, "Bus": 1,
    "truck": 2, "Truck": 2,
    "motorcycle": 3, "motorbike": 3, "bike": 3,
    "bicycle": 4, "Bicycle": 4,
    "rickshaw": 5, "Rickshaw": 5,
    "auto_rickshaw": 6, "cng": 6, "CNG": 6,
    "easy_bike": 7, "easybike": 7, "Easy_bike": 7,
    "van": 8, "Van": 8,
    "leguna": 9, "human_hauler": 9, "Leguna": 9,
    "pedestrian": 10, "person": 10, "Pedestrian": 10,
    "animal": 11, "cow": 11, "dog": 11, "goat": 11
}

def convert_box(size, box):
    """
    Converts XML (xmin, xmax) to YOLO (x_center, width) normalized.
    """
    dw = 1. / size[0]
    dh = 1. / size[1]
    
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)

def convert_xml_to_yolo():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    xml_files = [f for f in os.listdir(XML_DIR) if f.endswith('.xml')]
    
    print(f"🚀 Converting {len(xml_files)} XML files to YOLO format...")
    
    converted_count = 0
    
    for xml_file in tqdm(xml_files, desc="Converting"):
        in_file = open(os.path.join(XML_DIR, xml_file))
        out_file = open(os.path.join(OUTPUT_DIR, xml_file.replace('.xml', '.txt')), 'w')
        
        try:
            tree = ET.parse(in_file)
            root = tree.getroot()
            size = root.find('size')
            w = int(size.find('width').text)
            h = int(size.find('height').text)

            # Skip empty or broken images
            if w == 0 or h == 0:
                continue

            for obj in root.iter('object'):
                cls = obj.find('name').text
                # Handle spaces/capitalization
                cls = cls.strip()
                
                if cls not in CLASS_MAP:
                    # print(f"Skipping unknown class: {cls}") # Uncomment to debug
                    continue
                
                cls_id = CLASS_MAP[cls]
                xmlbox = obj.find('bndbox')
                b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), 
                     float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
                
                # Convert logic
                bb = convert_box((w, h), b)
                
                # Write YOLO line
                out_file.write(f"{cls_id} {bb[0]:.6f} {bb[1]:.6f} {bb[2]:.6f} {bb[3]:.6f}\n")
                
            converted_count += 1
            
        except Exception as e:
            print(f"❌ Error parsing {xml_file}: {e}")
        finally:
            in_file.close()
            out_file.close()
            
    print(f"✅ Successfully converted {converted_count} labels.")

if __name__ == "__main__":
    convert_xml_to_yolo()