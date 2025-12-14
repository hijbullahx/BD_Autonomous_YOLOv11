import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ultralytics import YOLO

# This is the blueprint Rony created
YAML_PATH = "models/yolov11_bd.yaml"

def verify_architecture():
    print("🏗️  Building Custom BD-YOLOv11 Architecture...")
    
    if not os.path.exists(YAML_PATH):
        print(f"❌ Error: {YAML_PATH} not found. Wait for Rony!")
        return

    # Initialize model from YAML (Random weights, just structure)
    try:
        model = YOLO(YAML_PATH)
        print("✅ Custom YAML loaded successfully.")
        
        # Check class count
        # Note: In some versions, model.names might still be default until trained,
        # but we check the config.
        print(f"   Network Config Classes: {model.cfg['nc'] if hasattr(model, 'cfg') else 'Custom'}")
        
        # Print info
        model.info()
        print("\n✅ The model architecture is ready for the thesis.")
        print("   (Note: We will still load pre-trained weights into this structure during training).")
        
    except Exception as e:
        print(f"❌ Architecture Verification Failed: {e}")

if __name__ == "__main__":
    verify_architecture()