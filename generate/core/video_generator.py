import os
import cv2
import numpy as np
from generate.utils.file_utils import FileUtils
from generate.config import VIDEO_WIDTH, VIDEO_HEIGHT, VIDEO_FPS, VIDEO_DURATION

class VideoGenerator:
    """影片檔案生成器"""

    def __init__(self, folder):
        self.folder = folder

    def generate(self):
        """生成隨機內容的影片"""
        FileUtils.create_directory(self.folder)
        filename = os.path.join(self.folder, f"{FileUtils.generate_random_string()}.avi")
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(filename, fourcc, VIDEO_FPS, (VIDEO_WIDTH, VIDEO_HEIGHT))

        for _ in range(int(VIDEO_FPS * VIDEO_DURATION)):
            frame = np.random.randint(0, 256, (VIDEO_HEIGHT, VIDEO_WIDTH, 3), dtype=np.uint8)
            out.write(frame)

        out.release()
        print(f"🎥 Generated video: {filename}")
