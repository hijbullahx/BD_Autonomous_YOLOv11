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
    
    # Augmentation Parameters (default values)
    MOSAIC = 1.0
    MIXUP = 0.1
    CUTMIX = 0.0
    COPY_PASTE = 0.0
    COPY_PASTE_MODE = "flip"
    AUTO_AUGMENT = "randaugment"
    ERASING = 0.4
    CROP_FRACTION = 1.0
    HSV_H = 0.015
    HSV_S = 0.7
    HSV_V = 0.4
    DEGREES = 0.0
    TRANSLATE = 0.1
    SCALE = 0.5
    SHEAR = 0.0
    PERSPECTIVE = 0.0
    FLIPUD = 0.0
    FLIPLR = 0.5
    BGIMAGE = 0.0
    MOSAIC_BORDER = [-320, -320]
    MIXUP_SCALE = [0.5, 1.5]
    MASK_RATIO = 4
    OVERLAP_MASK = True
    BGR = 0.0
    
    @staticmethod
    def get_args() -> dict:
        """
        Return augmentation hyperparameters as a dictionary.
        Useful for passing to model.train() with unpacking.
        """
        return {
            'mosaic': TrainingConfig.MOSAIC,
            'mixup': TrainingConfig.MIXUP,
            'cutmix': TrainingConfig.CUTMIX,
            'copy_paste': TrainingConfig.COPY_PASTE,
            'copy_paste_mode': TrainingConfig.COPY_PASTE_MODE,
            'auto_augment': TrainingConfig.AUTO_AUGMENT,
            'erasing': TrainingConfig.ERASING,
            'crop_fraction': TrainingConfig.CROP_FRACTION,
            'hsv_h': TrainingConfig.HSV_H,
            'hsv_s': TrainingConfig.HSV_S,
            'hsv_v': TrainingConfig.HSV_V,
            'degrees': TrainingConfig.DEGREES,
            'translate': TrainingConfig.TRANSLATE,
            'scale': TrainingConfig.SCALE,
            'shear': TrainingConfig.SHEAR,
            'perspective': TrainingConfig.PERSPECTIVE,
            'flipud': TrainingConfig.FLIPUD,
            'fliplr': TrainingConfig.FLIPLR,
            'bgimage': TrainingConfig.BGIMAGE,
            'mosaic_border': TrainingConfig.MOSAIC_BORDER,
            'mixup_scale': TrainingConfig.MIXUP_SCALE,
            'mask_ratio': TrainingConfig.MASK_RATIO,
            'overlap_mask': TrainingConfig.OVERLAP_MASK,
            'bgr': TrainingConfig.BGR,
        }
    
    @staticmethod
    def print_summary():
        """Print a summary of the training configuration."""
        print("📋 Training Configuration Summary:")
        print(f"   Data YAML: {TrainingConfig.DATA_YAML}")
        print(f"   Model YAML: {TrainingConfig.MODEL_YAML}")
        print(f"   Pre-trained Weights: {TrainingConfig.WEIGHTS}")
        print(f"   Epochs: {TrainingConfig.EPOCHS}")
        print(f"   Image Size: {TrainingConfig.IMG_SIZE}")
        print(f"   Batch Size: {TrainingConfig.BATCH_SIZE}")
        print(f"   Seed: {TrainingConfig.SEED}")
        print(f"   Augmentation: mosaic={TrainingConfig.MOSAIC}, mixup={TrainingConfig.MIXUP}")
