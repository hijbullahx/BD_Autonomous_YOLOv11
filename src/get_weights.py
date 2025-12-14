import os
from ultralytics import YOLO

MODEL_DIR = "models"
MODEL_NAME = "yolo11n.pt"

def download_weights():
    os.makedirs(MODEL_DIR, exist_ok=True)
    model_path = os.path.join(MODEL_DIR, MODEL_NAME)
    
    if os.path.exists(model_path):
        print(f"✅ Model {MODEL_NAME} already exists in {MODEL_DIR}")
        return

    print(f"⬇️ Downloading {MODEL_NAME}...")
    # Initialize YOLO class downloads the weights automatically if not found
    model = YOLO(MODEL_NAME) 
    
    # Move it to our models folder if it downloaded to root
    if os.path.exists(MODEL_NAME):
        os.rename(MODEL_NAME, model_path)
        
    print(f"✅ Weights saved to {model_path}")

if __name__ == "__main__":
    download_weights()