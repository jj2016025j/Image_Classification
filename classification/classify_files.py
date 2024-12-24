### file_classifier.py

import os
from classification import FileUtils

class FileClassifier:
    def __init__(self, source_dir, base_target_dir, extensions_mapping):
        self.source_dir = source_dir
        self.base_target_dir = base_target_dir
        self.extensions_mapping = extensions_mapping

    def create_directories(self):
        """
        創建目標子目錄
        """
        for subdir in self.extensions_mapping.keys():
            dir_path = os.path.join(self.base_target_dir, subdir)
            FileUtils.create_directory(dir_path)
        FileUtils.create_directory(os.path.join(self.base_target_dir, "other"))

    def get_target_directory(self, file_extension):
        """
        根據文件擴展名獲取目標目錄
        Args:
            file_extension (str): 文件擴展名
        Returns:
            str: 目標目錄名稱
        """
        for category, extensions in self.extensions_mapping.items():
            if file_extension in extensions:
                return category
        return "other"

    def move_files(self, current_dir):
        """
        移動文件到目標目錄
        Args:
            current_dir (str): 當前遍歷的目錄
        """
        for root, _, files in os.walk(current_dir):
            for filename in files:
                file_path = os.path.join(root, filename)
                if os.path.isfile(file_path):
                    file_extension = os.path.splitext(filename)[1].lower()
                    target_subdir = self.get_target_directory(file_extension)
                    target_dir = os.path.join(self.base_target_dir, target_subdir)
                    FileUtils.move_file(file_path, target_dir, filename)
                    print(f'Moved {filename} to {target_dir}')

    def classify_files(self):
        """
        主函數，用於分類文件並移動到相應目標目錄
        """
        self.create_directories()
        self.move_files(self.source_dir)
        FileUtils.clean_empty_directories(self.source_dir)