import os
import shutil

from file_operations.ensure_directory import ensure_directory_exists

class FileUtils:
    @staticmethod
    def create_directory(path):
        """
        創建目標資料夾
        Args:
            path (str): 目標資料夾路徑
        """
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"Created directory: {path}")

    @staticmethod
    def move_file(source_file, target_dir, image_name):
        """
        移動檔案到目標目錄，並處理重名問題
        Args:
            source_file (str): 源文件路徑
            target_dir (str): 目標目錄
            image_name (str): 文件名
        Returns:
            str: 目標文件路徑
        """
        target_path = os.path.join(target_dir, image_name)
        base_name, ext = os.path.splitext(image_name)
        i = 1

        while os.path.exists(target_path):
            target_path = os.path.join(target_dir, f"{base_name}_{i}{ext}")
            i += 1

        shutil.move(source_file, target_path)
        return target_path

    @staticmethod
    def move_file(source_file, target_dir, filename):
        """
        移動文件到目標目錄，並處理重名問題
        Args:
            source_file (str): 源文件路徑
            target_dir (str): 目標目錄
            filename (str): 文件名
        """
        FileUtils.create_directory(target_dir)
        target_path = os.path.join(target_dir, filename)
        base_name, ext = os.path.splitext(filename)
        i = 1

        while os.path.exists(target_path):
            target_path = os.path.join(target_dir, f"{base_name}_{i}{ext}")
            i += 1

        shutil.move(source_file, target_path)
        return target_path
    
    @staticmethod
    def print_stats(stats):
        """
        打印統計數據
        Args:
            stats (dict): 統計數據字典
        """
        for key, value in stats.items():
            print(f"{key}: {value}")

    @staticmethod
    def clean_empty_directories(directory):
        """
        清理空目錄
        Args:
            directory (str): 目錄路徑
        """
        for root, dirs, _ in os.walk(directory, topdown=False):
            for dir_name in dirs:
                dir_path = os.path.join(root, dir_name)
                if not os.listdir(dir_path):
                    os.rmdir(dir_path)
                    print(f"Removed empty directory: {dir_path}")
                    
def create_directory(path):
    """確保指定路徑存在，若不存在則創建"""
    if not os.path.exists(path):
        os.mkdir(path)

def move_file(source_file, target_dir, filename):
    """將文件移動到目標目錄"""
    create_directory(target_dir)
    shutil.move(source_file, os.path.join(target_dir, filename))

def clean_empty_directories(directory):
    """清除目錄中的空子目錄"""
    for root, dirs, _ in os.walk(directory, topdown=False):
        for subdir in dirs:
            dir_path = os.path.join(root, subdir)
            if not os.listdir(dir_path):
                os.rmdir(dir_path)