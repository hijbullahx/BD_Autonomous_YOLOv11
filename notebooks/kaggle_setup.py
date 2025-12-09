import sys
import os
import torch

# Add the project root to system path so we can import src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    from src.utils import set_seed
    print("✅ Import Successful: src.utils found.")
except ImportError:
    print("❌ ERROR: Could not import src.utils. Check directory structure.")

def check_environment():
    print("="*30)
    print("🇧🇩 BD Autonomous YOLOv11 Setup")
    print("="*30)
    
    # 1. Check Python Version
    print(f"Python Version: {sys.version.split()[0]}")
    
    # 2. Check GPU
    if torch.cuda.is_available():
        gpu_count = torch.cuda.device_count()
        gpu_name = torch.cuda.get_device_name(0)
        print(f"✅ GPU DETECTED: {gpu_name} (Count: {gpu_count})")
        print("Ready for YOLOv11 Training.")
    else:
        print("❌ WARNING: No GPU detected. Training will be extremely slow.")
        
    # 3. Set Seed
    if 'set_seed' in globals():
        set_seed(42)

if __name__ == "__main__":
    check_environment()