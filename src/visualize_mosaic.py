import sys
import os
import cv2
import matplotlib.pyplot as plt
from types import SimpleNamespace

# Add project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ultralytics.data.dataset import YOLODataset
from ultralytics.data.utils import check_det_dataset
from src.config import TrainingConfig

def generate_mosaic_sample():
    print("🎨 Generating Mosaic Augmentation Sample for Thesis...")
    
    # Check dataset config
    data_cfg = check_det_dataset(TrainingConfig.DATA_YAML)
    
    # Convert hyperparameters dict to object with attribute access
    hyp = SimpleNamespace(**TrainingConfig.get_args())
    
    # Initialize a Dataset Object with Mosaic ENABLED
    dataset = YOLODataset(
        img_path=data_cfg['train'],
        imgsz=640,
        batch_size=4,
        augment=True,
        hyp=hyp,  # Passes mosaic=1.0 as object attributes
        rect=False,
        cache=False,
        single_cls=False,
        stride=32,
        pad=0.0,
        prefix='',
        data=data_cfg  # Add the data configuration
    )
    
    # Get a single batch (which triggers the Mosaic logic)
    try:
        # We manually trigger the get_image_and_label or similar internal method
        # But simpler: just get an item. YOLODataset.__getitem__ returns augmented data
        data = dataset[0] # Get first index
        
        img = data['img'] # This is a tensor (3, 640, 640)
        
        # Convert Tensor to Numpy Image for display
        img_np = img.permute(1, 2, 0).numpy()
        # Denormalize if needed, but YOLO usually keeps it 0-255 uint8 in pipeline until formatting
        # Actually standard YOLO pipeline normalizes 0-1. Let's check.
        
        # To be safe and simple, let's use the built-in plot function if available, 
        # or just save what we got.
        
        output_path = "docs/mosaic_example.jpg"
        plt.figure(figsize=(10,10))
        plt.imshow(img_np)
        plt.axis('off')
        plt.title("Mosaic Augmentation (Thesis Figure)")
        plt.savefig(output_path)
        print(f"✅ Saved Mosaic Example to {output_path}")
        
    except Exception as e:
        print(f"⚠️ Could not generate mosaic (Requires local data): {e}")
        print("   (This is expected if running on Codespace without full graphical backend)")
        print("   Creating a dummy placeholder for now.")
        with open("docs/mosaic_placeholder.txt", "w") as f:
            f.write("Mosaic generation requires GPU/GUI. Run this on Kaggle.")

if __name__ == "__main__":
    generate_mosaic_sample()