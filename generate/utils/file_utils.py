import os
import random
import string

class FileUtils:
    """檔案工具類別"""

    @staticmethod
    def create_directory(directory):
        """建立資料夾"""
        os.makedirs(directory, exist_ok=True)

    @staticmethod
    def generate_random_string(length=12):
        """生成隨機檔案名稱"""
        characters = string.ascii_letters + string.digits + '_'
        return ''.join(random.choice(characters) for _ in range(length))
