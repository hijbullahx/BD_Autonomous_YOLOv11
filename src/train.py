import sys
import os
import torch

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ultralytics import YOLO
from src.config import TrainingConfig
from src.callbacks import get_callbacks

def train_model():
    print("🚀 Starting YOLOv11 BD-Traffic Training...")
    
    # 1. Load the Custom Architecture
    model = YOLO("models/yolov11_bd.yaml")
    
    # 2. Load Weights
    try:
        model.load("models/yolo11n.pt")
        print("✅ Pre-trained weights loaded.")
    except Exception as e:
        print(f"⚠️ Warning: {e}")

    # 3. REGISTER CALLBACKS (The Correct Way)
    # We attach our custom "Rickshaw Tracker" before training starts
    callbacks = get_callbacks()
    for event, func in callbacks.items():
        model.add_callback(event, func)
    print("✅ Custom Callbacks registered.")

    # 4. Get Hyperparameters
    args = TrainingConfig.get_args()
    
    # 5. Start Training
    results = model.train(
        data=TrainingConfig.DATA_YAML,
        epochs=TrainingConfig.EPOCHS,
        imgsz=TrainingConfig.IMG_SIZE,
        batch=TrainingConfig.BATCH_SIZE,
        seed=TrainingConfig.SEED,
        project="runs/train",
        name="bd_yolo11_experiment",
        exist_ok=True,
        pretrained=True,
        optimizer="auto",
        verbose=True,
        
        # Augmentation (Unpacked from config)
        **args,
        
        # Hardware
        device=0 if torch.cuda.is_available() else "cpu",
        workers=2
    )
    
    print("🏁 Training Cycle Complete.")

if __name__ == "__main__":
    train_model()