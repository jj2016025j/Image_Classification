import os
from PIL import Image
import random
from file_operations.file_utils import create_directory, generate_random_string

def generate_image(folder, size=(100, 100), color=(255, 0, 0)):
    """Generate an image with specified size and color."""
    create_directory(folder)
    filename = os.path.join(folder, generate_random_string() + '.png')
    image = Image.new('RGB', size, color)
    image.save(filename)
    print(f"Generated image: {filename}")

def generate_random_images(folder, min_size=(50, 50), max_size=(500, 500), color=(255, 0, 0)):
    """Generate an image with random size."""
    create_directory(folder)
    width = random.randint(min_size[0], max_size[0])
    height = random.randint(min_size[1], max_size[1])
    filename = os.path.join(folder, generate_random_string() + '.png')
    image = Image.new('RGB', (width, height), color)
    image.save(filename)
    print(f"Generated image: {filename}, Size: {width}x{height}")
