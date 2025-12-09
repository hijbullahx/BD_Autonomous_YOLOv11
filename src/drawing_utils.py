import cv2
import random
import numpy as np

# Unique colors for 12 classes to make them distinct
COLORS = [
    (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0),
    (0, 255, 255), (255, 0, 255), (192, 192, 192), (128, 0, 0),
    (128, 128, 0), (0, 128, 0), (128, 0, 128), (0, 128, 128)
]

def draw_yolo_bbox(image, bbox, class_id, class_name):
    """
    Draws a single YOLO format bounding box on the image.
    bbox: [x_center, y_center, width, height] (Normalized 0-1)
    """
    h, w, _ = image.shape
    x_c, y_c, bw, bh = bbox
    
    # Convert YOLO (Normalized) to Pixel Coordinates
    x1 = int((x_c - bw / 2) * w)
    y1 = int((y_c - bh / 2) * h)
    x2 = int((x_c + bw / 2) * w)
    y2 = int((y_c + bh / 2) * h)
    
    # Get Color
    color = COLORS[int(class_id) % len(COLORS)]
    
    # Draw Rectangle
    cv2.rectangle(image, (x1, y1), (x2, y2), color, 2)
    
    # Draw Label Background
    label = f"{class_name}"
    (tw, th), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
    cv2.rectangle(image, (x1, y1 - 20), (x1 + tw, y1), color, -1)
    
    # Draw Text
    cv2.putText(image, label, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
    
    return image