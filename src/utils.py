import random
import os
import numpy as np
import torch

def set_seed(seed=42):
    """
    Sets the random seed for reproducibility across Python, NumPy, and PyTorch.
    
    Args:
        seed (int): The seed value to use. Default is 42.
    """
    random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)  # if you are using multi-GPU.
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False
    
    print(f"[INFO] Random seed set to {seed}. Work is reproducible.")

if __name__ == "__main__":
    set_seed()