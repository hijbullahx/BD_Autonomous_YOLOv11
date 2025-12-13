import os
import shutil
from tqdm import tqdm

SOURCE_DIR = "data/raw"
DEST_DIR = "data/processed"

def organize_files():
    # Create standard YOLO folders
    os.makedirs(os.path.join(DEST_DIR, "images"), exist_ok=True)
    os.makedirs(os.path.join(DEST_DIR, "labels"), exist_ok=True) # For when we convert later
    os.makedirs(os.path.join(DEST_DIR, "xml_raw"), exist_ok=True) # Temporary storage for XML
    
    print("🚀 Moving files to flat structure...")
    
    files_moved = 0
    
    for root, dirs, files in os.walk(SOURCE_DIR):
        for file in tqdm(files, desc="Moving"):
            src_path = os.path.join(root, file)
            
            # Handle Images
            if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                # Create a unique name to prevent overwriting (some datasets reuse names)
                # We prepend the folder name to make it unique
                folder_name = os.path.basename(root)
                new_name = f"{folder_name}_{file}"
                
                dest_path = os.path.join(DEST_DIR, "images", new_name)
                shutil.copy2(src_path, dest_path)
                files_moved += 1
            
            # Handle XML Labels
            elif file.lower().endswith('.xml'):
                folder_name = os.path.basename(root)
                new_name = f"{folder_name}_{file}"
                
                dest_path = os.path.join(DEST_DIR, "xml_raw", new_name)
                shutil.copy2(src_path, dest_path)

    print(f"✅ Organized {files_moved} images into {DEST_DIR}/images")

if __name__ == "__main__":
    organize_files()