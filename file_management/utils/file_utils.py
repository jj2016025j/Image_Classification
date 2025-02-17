import os
import uuid
import random
import string
from datetime import datetime

class FileUtils:
    """ 檔案工具類 """

    @staticmethod
    def generate_random_string(length=12):
        """ 產生隨機檔案名稱 """
        characters = string.ascii_letters + string.digits + '_'
        return ''.join(random.choice(characters) for _ in range(length))

    @staticmethod
    def create_directory(folder):
        """ 建立資料夾 """
        if not os.path.exists(folder):
            os.makedirs(folder)
            
def generate_uuid4_filename(output_dir, prefix="image"):
    """生成 UUID4 命名的唯一檔案名稱"""
    create_directory(output_dir)
    return os.path.join(output_dir, f"{prefix}_{uuid.uuid4().hex}.png")

def generate_time_based_filename(output_dir, prefix="image"):
    """生成時間戳記命名的唯一檔案名稱"""
    current_time = datetime.now()
    time_string = current_time.strftime("%Y%m%d_%H%M%S_%f")
    create_directory(output_dir)
    return os.path.join(output_dir, f"{prefix}_{time_string}.png")

def generate_filename_by_model(output_dir, model_name="model"):
    """根據模型名稱生成唯一檔案名稱"""
    return generate_time_based_filename(output_dir, prefix=model_name)
