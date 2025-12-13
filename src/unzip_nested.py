import os
import zipfile
from tqdm import tqdm

ROOT_DIR = "data/raw"

def unzip_nested_zips():
    print(f"🕵️ Searching for nested .zip files in {ROOT_DIR}...")
    
    zip_files = []
    # 1. Find all zip files
    for root, dirs, files in os.walk(ROOT_DIR):
        for file in files:
            if file.endswith(".zip"):
                zip_files.append(os.path.join(root, file))
    
    print(f"📦 Found {len(zip_files)} nested zip files. Extracting now...")
    
    # 2. Extract each one
    for zip_path in tqdm(zip_files, desc="Unzipping"):
        try:
            # Extract to the SAME folder where the zip is
            extract_to = os.path.dirname(zip_path)
            
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(extract_to)
            
            # Optional: Delete the zip after extracting to save space
            os.remove(zip_path)
            
        except zipfile.BadZipFile:
            print(f"❌ Error: Bad zip file {zip_path}")
        except Exception as e:
            print(f"⚠️ Warning: Could not unzip {zip_path}: {e}")

    print("✅ Nested unzipping complete.")

if __name__ == "__main__":
    unzip_nested_zips()