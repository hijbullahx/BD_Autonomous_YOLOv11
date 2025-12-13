import os
import sys

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.download_utils import download_file
from src.ingest_data import extract_data

# The Direct Link to the Zip file from Mendeley Data
DATASET_URL = "https://prod-dcd-datasets-cache-zipfiles.s3.eu-west-1.amazonaws.com/h8bfgtdp2r-6.zip"
ZIP_PATH = "data/raw/dataset.zip"
EXTRACT_PATH = "data/raw/"

def main():
    print("🚀 Starting Dataset Setup Pipeline...")
    
    # 1. Create Folder
    os.makedirs("data/raw", exist_ok=True)
    
    # 2. Download
    if not os.path.exists(ZIP_PATH):
        download_file(DATASET_URL, ZIP_PATH)
    else:
        print("ℹ️ Zip file already exists. Skipping download.")
        
    # 3. Extract
    print("📦 Extracting data...")
    extract_data(ZIP_PATH, EXTRACT_PATH)
    
    print("✅ Dataset Setup Complete. Check data/raw/")

if __name__ == "__main__":
    main()git commit -m "P2.T2: Added master dataset setup script - Hijbullah"