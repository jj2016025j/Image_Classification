# file: file_utils.py
import uuid
from datetime import datetime
import os
import random
import string

def generate_uuid4_filename(output_dir, prefix="image"):
    """Generate a UUID4-based unique filename."""
    return os.path.join(output_dir, f"{prefix}_{uuid.uuid4().hex}.png")

def generate_time_based_filename(output_dir, prefix="image"):
    """Generate a timestamp-based unique filename."""
    current_time = datetime.now()
    time_string = current_time.strftime("%Y%m%d_%H%M%S_%f")
    os.makedirs(output_dir, exist_ok=True)
    return os.path.join(output_dir, f"{prefix}_{time_string}.png")

def generate_random_string(length=12):
    """Generate a random string of specified length."""
    characters = string.ascii_letters + string.digits + '_'
    return ''.join(random.choice(characters) for _ in range(length))

def create_directory(folder):
    """Create directory if it doesn't exist."""
    if not os.path.exists(folder):
        os.makedirs(folder)