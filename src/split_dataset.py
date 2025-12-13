import os
import shutil
import random
from tqdm import tqdm

# Paths
DATA_DIR = "data/processed"
IMG_DIR = os.path.join(DATA_DIR, "images")
LBL_DIR = os.path.join(DATA_DIR, "labels")

def split_data(train_ratio=0.7, val_ratio=0.2):
    print("🚀 Starting Dataset Split...")
    
    # 1. Identify valid pairs (Image + Label)
    images = [f for f in os.listdir(IMG_DIR) if f.endswith(('.jpg', '.png', '.jpeg'))]
    valid_pairs = []
    
    print(f"🔎 Scanning {len(images)} images for labels...")
    
    for img in tqdm(images):
        # Check if corresponding text file exists
        label_name = os.path.splitext(img)[0] + ".txt"
        label_path = os.path.join(LBL_DIR, label_name)
        
        if os.path.exists(label_path):
            valid_pairs.append(img)
            
    print(f"✅ Found {len(valid_pairs)} valid image-label pairs.")
    print(f"🗑️  Discarding {len(images) - len(valid_pairs)} orphan images.")
    
    # 2. Shuffle
    random.seed(42)
    random.shuffle(valid_pairs)
    
    # 3. Calculate split indices
    n = len(valid_pairs)
    n_train = int(n * train_ratio)
    n_val = int(n * val_ratio)
    # n_test is the rest
    
    train_files = valid_pairs[:n_train]
    val_files = valid_pairs[n_train:n_train + n_val]
    test_files = valid_pairs[n_train + n_val:]
    
    # 4. Move files function
    def move_files(file_list, split_name):
        # Create directories: data/processed/train/images, data/processed/train/labels
        split_img_dir = os.path.join(DATA_DIR, split_name, "images")
        split_lbl_dir = os.path.join(DATA_DIR, split_name, "labels")
        os.makedirs(split_img_dir, exist_ok=True)
        os.makedirs(split_lbl_dir, exist_ok=True)
        
        for img in tqdm(file_list, desc=f"Moving to {split_name}"):
            label = os.path.splitext(img)[0] + ".txt"
            
            # Move Image
            shutil.move(os.path.join(IMG_DIR, img), os.path.join(split_img_dir, img))
            # Move Label
            shutil.move(os.path.join(LBL_DIR, label), os.path.join(split_lbl_dir, label))
            
    # 5. Execute Moves
    move_files(train_files, "train")
    move_files(val_files, "val")
    move_files(test_files, "test")
    
    # 6. Cleanup empty folders
    try:
        os.rmdir(IMG_DIR)
        os.rmdir(LBL_DIR)
    except:
        pass # Folders might not be empty if orphans remain
        
    print("✨ Dataset Split Complete!")
    print(f"   Train: {len(train_files)}")
    print(f"   Val:   {len(val_files)}")
    print(f"   Test:  {len(test_files)}")

if __name__ == "__main__":
    split_data()