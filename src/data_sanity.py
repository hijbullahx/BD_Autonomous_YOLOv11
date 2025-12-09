import os
import glob

def check_dataset_balance(dir_path):
    """
    Checks if every image has a corresponding label file.
    Args:
        dir_path (str): Path to the dataset directory (e.g., 'data/processed/train')
    """
    print(f"🔎 Checking directory: {dir_path}")
    
    if not os.path.exists(dir_path):
        print(f"❌ Error: Directory '{dir_path}' does not exist yet.")
        return

    # specific paths
    img_path = os.path.join(dir_path, 'images')
    lbl_path = os.path.join(dir_path, 'labels')

    if not os.path.exists(img_path) or not os.path.exists(lbl_path):
        print("❌ Error: 'images' or 'labels' subfolder missing.")
        return

    # Get file lists
    images = sorted(glob.glob(os.path.join(img_path, '*.jpg')) + glob.glob(os.path.join(img_path, '*.png')))
    labels = sorted(glob.glob(os.path.join(lbl_path, '*.txt')))

    num_imgs = len(images)
    num_lbls = len(labels)

    print(f"   🖼️ Images found: {num_imgs}")
    print(f"   📝 Labels found: {num_lbls}")

    if num_imgs == num_lbls:
        print("   ✅ MATCH: Image and Label counts are equal.")
    else:
        print(f"   ⚠️ WARNING: Mismatch detected! ({abs(num_imgs - num_lbls)} missing files)")

if __name__ == "__main__":
    # Test on a dummy path
    check_dataset_balance("data/processed/train")