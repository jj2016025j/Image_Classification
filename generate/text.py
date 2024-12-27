import os
from file.utils import generate_random_string, create_directory

def generate_text_file(folder, content="Hello, world!"):
    """Generate a text file with specified content."""
    create_directory(folder)
    filename = os.path.join(folder, generate_random_string() + '.txt')
    with open(filename, 'w') as file:
        file.write(content)
    print(f"Generated text file: {filename}")
