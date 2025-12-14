import sys
import os
import yaml
from pathlib import Path

# Ensure project root is in the import path for local modules if needed
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ultralytics import YOLO

# This is the blueprint Rony created
YAML_PATH = Path("models/yolov11_bd.yaml")


def _read_nc_from_yaml(yaml_path: Path) -> str:
    """Safely read `nc` from the YAML file without relying on ultralytics internals."""
    try:
        cfg = yaml.safe_load(yaml_path.read_text())
        return cfg.get("nc", "(missing)") if isinstance(cfg, dict) else "(invalid)"
    except Exception:
        return "(unreadable)"


def verify_architecture():
    print("🏗️  Building Custom BD-YOLOv11 Architecture...")

    if not YAML_PATH.exists():
        print(f"❌ Error: {YAML_PATH} not found. Wait for Rony!")
        return

    # Initialize model from YAML (random weights, just structure)
    try:
        nc_value = _read_nc_from_yaml(YAML_PATH)
        model = YOLO(str(YAML_PATH))
        print("✅ Custom YAML loaded successfully.")

        # Report class count from YAML for clarity
        print(f"   Network Config Classes (nc): {nc_value}")

        # Print info
        model.info()
        print("\n✅ The model architecture is ready for the thesis.")
        print("   (Note: We will still load pre-trained weights into this structure during training).")

    except Exception as e:
        print(f"❌ Architecture Verification Failed: {e}")


if __name__ == "__main__":
    verify_architecture()