"""
Training configuration for BD-YOLOv11 model.
Centralized hyperparameters and settings.
"""

class TrainingConfig:
    """Hyperparameters and training settings for BD traffic detection model."""
    
    # Data & Model
    DATA_YAML = "data/bd_traffic.yaml"
    MODEL_YAML = "models/yolov11_bd.yaml"
    WEIGHTS = "models/yolo11n.pt"
    
    # Training Parameters
    EPOCHS = 50
    IMG_SIZE = 640
    BATCH_SIZE = 16
    SEED = 42
    
    # Augmentation Parameters (Supported by YOLOv11 Detection)
    # -------------------------------------------------------
    MOSAIC = 1.0        # Thesis Strategy: High for occlusion
    MIXUP = 0.1         # Thesis Strategy: Moderate for overlap
    COPY_PASTE = 0.0    # Optional
    
    # Photometric
    HSV_H = 0.015
    HSV_S = 0.7
    HSV_V = 0.4
    
    # Geometric
    DEGREES = 0.0
    TRANSLATE = 0.1
    SCALE = 0.5
    SHEAR = 0.0
    PERSPECTIVE = 0.0
    FLIPUD = 0.0
    FLIPLR = 0.5
    
    # Advanced (Removed invalid keys for stability)
    # CUTMIX = 0.0      # Classification only
    # BGIMAGE = 0.0     # Classification only
    
    @staticmethod
    def get_args() -> dict:
        """
        Return ONLY valid augmentation hyperparameters for model.train()
        """
        return {
            'mosaic': TrainingConfig.MOSAIC,
            'mixup': TrainingConfig.MIXUP,
            'copy_paste': TrainingConfig.COPY_PASTE,
            
            # Photometric
            'hsv_h': TrainingConfig.HSV_H,
            'hsv_s': TrainingConfig.HSV_S,
            'hsv_v': TrainingConfig.HSV_V,
            
            # Geometric
            'degrees': TrainingConfig.DEGREES,
            'translate': TrainingConfig.TRANSLATE,
            'scale': TrainingConfig.SCALE,
            'shear': TrainingConfig.SHEAR,
            'perspective': TrainingConfig.PERSPECTIVE,
            'flipud': TrainingConfig.FLIPUD,
            'fliplr': TrainingConfig.FLIPLR,
        }
    
    @staticmethod
    def print_summary():
        print("📋 Training Configuration Summary:")
        print(f"   Epochs: {TrainingConfig.EPOCHS}")
        print(f"   Augmentation: mosaic={TrainingConfig.MOSAIC}, mixup={TrainingConfig.MIXUP}")