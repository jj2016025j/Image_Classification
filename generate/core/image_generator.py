import os
import random
from PIL import Image
from generate.utils.file_utils import FileUtils
from generate.config import IMAGE_MIN_SIZE, IMAGE_MAX_SIZE

class ImageGenerator:
    """圖片檔案生成器"""

    def __init__(self, folder):
        self.folder = folder

    def generate(self):
        """生成固定大小與顏色的圖片"""
        FileUtils.create_directory(self.folder)
        size = IMAGE_MIN_SIZE  # 固定大小
        filename = os.path.join(self.folder, f"{FileUtils.generate_random_string()}.png")
        image = Image.new('RGB', size, (0, 0, 0))
        image.save(filename)
        print(f"🖼 Generated image: {filename}")

    def generate_random(self):
        """生成隨機尺寸的圖片"""
        FileUtils.create_directory(self.folder)
        width = random.randint(*IMAGE_MIN_SIZE)
        height = random.randint(*IMAGE_MAX_SIZE)
        filename = os.path.join(self.folder, f"{FileUtils.generate_random_string()}.png")
        image = Image.new('RGB', (width, height), (0, 0, 0))
        image.save(filename)
        print(f"🖼 Generated image: {filename}, Size: {width}x{height}")
