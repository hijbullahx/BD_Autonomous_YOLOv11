import sys
import os
# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ultralytics import YOLO

# Path to the weights Rony is downloading
WEIGHTS_PATH = "models/yolo11n.pt"

def init_model():
    print("🧠 Initializing YOLOv11 for BD Traffic...")
    
    if not os.path.exists(WEIGHTS_PATH):
        print(f"❌ Error: Weights not found at {WEIGHTS_PATH}. Run Rony's script first!")
        return

    # Load the pre-trained model
    model = YOLO(WEIGHTS_PATH)
    
    # Print the "Before" state
    print(f"   Original Classes: {len(model.names)} (COCO defaults)")
    
    # We don't actually 'change' the weights file here, 
    # but we verify that we can load it.
    # The class override happens during training (task P3.T3).
    
    # Print Model Summary
    print("\n📊 Model Architecture Summary:")
    model.info()
    
    print("\n✅ Model loaded successfully. Ready for Transfer Learning.")

if __name__ == "__main__":
    init_model()