import os
import cv2
import numpy as np
from file_utils import generate_random_string, create_directory

def generate_video(folder, width=640, height=480, fps=30, duration=5):
    """Generate a video with random content."""
    create_directory(folder)
    filename = os.path.join(folder, generate_random_string() + '.avi')
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(filename, fourcc, fps, (width, height))
    
    for _ in range(int(fps * duration)):
        frame = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
        out.write(frame)
    
    out.release()
    print(f"Generated video: {filename}")
