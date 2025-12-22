import sys
import os
import torch
from src.callbacks import get_callbacks
# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ultralytics import YOLO
from src.config import TrainingConfig

def train_model():
    print("🚀 Starting YOLOv11 BD-Traffic Training...")
    
    # 1. Load the Custom Architecture (The Skeleton)
    # We load the YAML to define the structure
    model = YOLO("models/yolov11_bd.yaml")
    
    # 2. Load Pre-trained Weights (The Knowledge)
    # We transfer weights from COCO to our skeleton
    # Note: It will warn about shape mismatch (80 vs 12 classes). This is EXPECTED.
    try:
        model.load("models/yolo11n.pt")
        print("✅ Pre-trained weights loaded into custom architecture.")
    except Exception as e:
        print(f"⚠️ Warning during weight loading: {e}")
        print("   (This is normal if changing class counts).")

    # 3. Get Hyperparameters
    args = TrainingConfig.get_args()
    
    # 4. Start Training
    # We use the config constants
    results = model.train(
        data=TrainingConfig.DATA_YAML,
        epochs=TrainingConfig.EPOCHS,
        imgsz=TrainingConfig.IMG_SIZE,
        batch=TrainingConfig.BATCH_SIZE,
        seed=TrainingConfig.SEED,
        project="runs/train",
        name="bd_yolo11_experiment",
        exist_ok=True,       # Overwrite existing folder
        pretrained=True,
        optimizer="auto",
        verbose=True,
        workers=2,
        
        # Augmentation Hyperparameters (From config.py)
        mosaic=args['mosaic'],
        mixup=args['mixup'],
        hsv_h=args['hsv_h'],
        hsv_s=args['hsv_s'],
        hsv_v=args['hsv_v'],
        degrees=args['degrees'],
        translate=args['translate'],
        scale=args['scale'],
        fliplr=args['fliplr'],
        callbacks=get_callbacks()
        
        # Hardware
        device=0 if torch.cuda.is_available() else "cpu",
        workers=2 
    )
    
    print("🏁 Training Cycle Complete. Check runs/train/bd_yolo11_experiment")

if __name__ == "__main__":
    train_model()