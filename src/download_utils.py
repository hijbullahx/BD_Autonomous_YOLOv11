import requests
import os
from tqdm import tqdm

def download_file(url, destination_path):
    """
    Downloads a file from a URL with a progress bar.
    """
    print(f"⬇️ Downloading from {url}...")
    
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024 # 1 Kibibyte

    with open(destination_path, 'wb') as file, tqdm(
        desc=destination_path,
        total=total_size,
        unit='iB',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for data in response.iter_content(block_size):
            size = file.write(data)
            bar.update(size)
            
    print(f"✅ Download complete: {destination_path}")

if __name__ == "__main__":
    # Test URL (Small text file)
    download_file("https://www.google.com/robots.txt", "robots.txt")