from ultralytics.utils import LOGGER

def on_train_epoch_end(trainer):
    """
    Custom Callback to log Rickshaw and CNG performance specifically.
    """
    # Ultralytics metrics are stored in trainer.metrics
    # Keys usually look like 'metrics/mAP50(B)'
    
    metrics = trainer.metrics
    epoch = trainer.epoch + 1
    
    # We want to highlight specific classes if possible.
    # Note: Accessing per-class mAP inside a callback is complex in YOLOv8/11 
    # without running a full validation. 
    # So we will log the Overall mAP with a special Thesis Message.
    
    map50 = metrics.get("metrics/mAP50(B)", 0)
    map50_95 = metrics.get("metrics/mAP50-95(B)", 0)
    
    LOGGER.info(f"\n🇧🇩 THESIS TRACKER (Epoch {epoch}):")
    LOGGER.info(f"   📈 Overall mAP@50:    {map50:.4f}")
    LOGGER.info(f"   🎯 High Precision mAP:{map50_95:.4f}")
    LOGGER.info("   (Check TensorBoard for Class 5: Rickshaw specific curves)\n")

def get_callbacks():
    """Returns a dict of callbacks to inject into the model."""
    return {
        "on_train_epoch_end": on_train_epoch_end
    }