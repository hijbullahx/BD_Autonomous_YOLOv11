import yaml
import os
import sys

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def load_class_names(yaml_path):
    """
    Loads class names from the data.yaml file.
    """
    if not os.path.exists(yaml_path):
        print(f"❌ Error: YAML file not found at {yaml_path}")
        return {}
        
    with open(yaml_path, 'r') as f:
        data = yaml.safe_load(f)
        
    return data.get('names', {})

if __name__ == "__main__":
    # Test path
    yaml_file = "data/bd_traffic.yaml"
    names = load_class_names(yaml_file)
    
    print(f"✅ Loaded {len(names)} classes from {yaml_file}")
    print(f"   Class 5: {names.get(5, 'Unknown')}")
    print(f"   Class 7: {names.get(7, 'Unknown')}")