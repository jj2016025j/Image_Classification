import os
from file_management.core.file_operations import FileOperations

class FileClassifier:
    """檔案分類器，負責根據文件擴展名進行分類"""

    def __init__(self, source_dir, base_target_dir, extensions_mapping):
        self.source_dir = source_dir
        self.base_target_dir = base_target_dir
        self.extensions_mapping = extensions_mapping

    def create_directories(self):
        """創建目標分類資料夾"""
        for subdir in self.extensions_mapping.keys():
            dir_path = os.path.join(self.base_target_dir, subdir)
            FileOperations.create_directory(dir_path)
        FileOperations.create_directory(os.path.join(self.base_target_dir, "other"))

    def get_target_directory(self, file_extension):
        """根據檔案副檔名返回對應的分類目錄"""
        for category, extensions in self.extensions_mapping.items():
            if file_extension in extensions:
                return category
        return "other"

    def move_files(self):
        """分類並移動文件到對應目錄"""
        for file_path in FileOperations.get_all_files_in_directory(self.source_dir):
            if os.path.isfile(file_path):
                file_extension = os.path.splitext(file_path)[1].lower()
                target_subdir = self.get_target_directory(file_extension)
                target_dir = os.path.join(self.base_target_dir, target_subdir)
                FileOperations.move_file(file_path, target_dir)

    def classify_files(self):
        """執行分類流程"""
        self.create_directories()
        self.move_files()
        FileOperations.clean_empty_directories(self.source_dir)

    def classify_files(self):
        """ 遍歷文件並分類 """
        for root, _, files in os.walk(self.source_dir):
            for filename in files:
                file_path = os.path.join(root, filename)
                file_extension = os.path.splitext(filename)[1].lower()
                target_subdir = self.get_target_directory(file_extension)
                target_path = os.path.join(self.target_dir, target_subdir)
                FileOperations.create_directory(target_path)
                FileOperations.move_file(file_path, target_path)