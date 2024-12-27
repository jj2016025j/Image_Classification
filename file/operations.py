# modules/file_operations.py
import os
import shutil

from classification.is_similar import is_similar

class FileOperations:
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
    def move_file(source_file, target_dir, filename):
        """
        移動檔案到目標目錄，並處理重名問題
        Args:
            source_file (str): 源文件路徑
            target_dir (str): 目標目錄
            filename (str): 文件名
        Returns:
            str: 目標文件路徑
        """
        FileOperations.create_directory(target_dir)
        target_path = os.path.join(target_dir, filename)
        base_name, ext = os.path.splitext(filename)
        i = 1

        while os.path.exists(target_path):
            target_path = os.path.join(target_dir, f"{base_name}_{i}{ext}")
            i += 1

        shutil.move(source_file, target_path)
        return target_path

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

    @staticmethod
    def process_directory(target_path):
        """
        處理指定目錄下的圖片
        :param target_path: 目標目錄的路徑
        """
        for root, dirs, files in os.walk(target_path):
            if root != target_path:
                for file in files:
                    file_path = os.path.join(root, file)
                    target_file_path = os.path.join(target_path, file)

                    if os.path.exists(target_file_path):
                        if is_similar(file_path, target_file_path):
                            os.remove(file_path)
                            print(f"Removed duplicate: {file_path}")
                    else:
                        shutil.move(file_path, target_file_path)
                        print(f"Moved: {file_path} -> {target_file_path}")

                shutil.rmtree(root)
                print(f"Removed directory: {root}")