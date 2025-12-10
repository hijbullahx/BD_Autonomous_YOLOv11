# Thesis Experiment Design: BD Autonomous YOLOv11

## 1. Problem Statement
Dhaka traffic is characterized by **unstructured lanes** and **high occlusion** (overlap). Standard models trained on COCO fail to distinguish between a Rickshaw and a CNG when they are touching.

## 2. Proposed Solution
We will implement an **Occlusion-Resistant YOLOv11** using specific augmentation strategies.

## 3. Experiment Roadmap

### Experiment A: The Baseline (COCO Transfer)
- **Model:** YOLOv11n (Nano) pretrained on COCO.
- **Data:** BD Traffic Dataset (Raw).
- **Hypothesis:** Will fail on Rickshaws and overlapped vehicles.

### Experiment B: BD-Adapted Training
- **Model:** YOLOv11n fine-tuned.
- **Classes:** 12 Custom Classes (Rickshaw, Easy_Bike, etc.).
- **Hypothesis:** Improved detection of local vehicles, but poor performance in heavy traffic jams.

### Experiment C: The Occlusion Specialist (Final Proposed Model)
- **Model:** YOLOv11n + Aggressive Augmentation.
- **Technique:** - **Mosaic Augmentation (1.0):** Forces model to learn context and small objects.
  - **MixUp (0.1):** Blends images to handle transparency/overlap.
- **Hypothesis:** Highest mAP@0.50 in heavy traffic scenarios.