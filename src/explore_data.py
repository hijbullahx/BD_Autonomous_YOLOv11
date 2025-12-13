import os

def count_files(start_path):
    print(f"🔎 Scanning {start_path}...")
    
    img_count = 0
    xml_count = 0
    txt_count = 0
    
    for root, dirs, files in os.walk(start_path):
        for file in files:
            if file.endswith(('.jpg', '.jpeg', '.png')):
                img_count += 1
            elif file.endswith('.xml'):
                xml_count += 1
            elif file.endswith('.txt'):
                txt_count += 1
                
    print(f"📊 Report:")
    print(f"   Images: {img_count}")
    print(f"   XML Labels: {xml_count}")
    print(f"   TXT Labels: {txt_count}")
    
    if xml_count > 0 and txt_count == 0:
        print("⚠️ NOTE: Data uses XML (VOC format). We will need to convert to TXT (YOLO).")

if __name__ == "__main__":
    count_files("data/raw")