import os
import zipfile
from tqdm import tqdm

def extract_data(zip_path, extract_to):
    """
    Extracts a zip file with a progress bar.
    """
    if not os.path.exists(zip_path):
        print(f"❌ Error: File {zip_path} not found.")
        return

    print(f"📂 Extracting {zip_path}...")
    
    # Ensure destination exists
    os.makedirs(extract_to, exist_ok=True)

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        # Get list of files for progress bar
        file_list = zip_ref.namelist()
        
        for file in tqdm(file_list, desc="Unzipping"):
            zip_ref.extract(file, extract_to)
            
    print(f"✅ Extraction complete. Data is in {extract_to}")

if __name__ == "__main__":
    # Example usage for testing
    # You would run this like: python src/ingest_data.py
    print("Run this script by importing the function or editing the path.")