import os
import sys
import urllib.request
import shutil
from pathlib import Path

MODEL_DIR = "models"
MODEL_NAME = "yolo11n.pt"
HF_URL = "https://huggingface.co/ultralytics/yolo11/resolve/main/yolo11n.pt"

def download_weights():
    os.makedirs(MODEL_DIR, exist_ok=True)
    model_path = os.path.join(MODEL_DIR, MODEL_NAME)

    if os.path.exists(model_path):
        print(f"✅ Model {MODEL_NAME} already exists in {MODEL_DIR}")
        return

    print(f"⬇️ Downloading {MODEL_NAME} from Hugging Face...")
    tmp_path = os.path.join(MODEL_DIR, f".{MODEL_NAME}.download")
    try:
        with urllib.request.urlopen(HF_URL) as response, open(tmp_path, "wb") as out_file:
            shutil.copyfileobj(response, out_file)
        Path(tmp_path).rename(model_path)
        print(f"✅ Weights saved to {model_path}")
    except Exception as e:
        print(f"❌ Failaed to download weights: {e}")
        print("If the issue persists, you can manually download and place the file here:")
        print(f"   {model_path}")
        print("Suggested command:")
        print(f"   wget -O {model_path} {HF_URL}")
        sys.exit(1)

if __name__ == "__main__":
    download_weights()