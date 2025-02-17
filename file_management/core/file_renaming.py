import os
from collections import defaultdict
from file_management.utils.file_utils import generate_random_string

class FileRenaming:
    """檔案批次重命名工具"""

    def __init__(self, directory):
        self.directory = directory
        self.extension_counts = defaultdict(int)

    def get_file_extension(self, filename):
        """取得檔案的副檔名"""
        return os.path.splitext(filename)[1].lower()

    def generate_new_filename(self, filename):
        """根據檔案副檔名產生新的唯一檔名"""
        file_extension = self.get_file_extension(filename)
        self.extension_counts[file_extension] += 1

        base_name = f"{file_extension[1:]}_{self.extension_counts[file_extension]}"
        new_filename = f"{base_name}{file_extension}"
        new_filepath = os.path.join(self.directory, new_filename)

        # 避免重複名稱，添加額外的編號
        counter = 1
        while os.path.exists(new_filepath):
            new_filename = f"{base_name}_{counter}{file_extension}"
            new_filepath = os.path.join(self.directory, new_filename)
            counter += 1

        return new_filename, new_filepath

    def rename_file(self, old_filepath, new_filepath, filename, new_filename):
        """執行檔案重命名"""
        os.rename(old_filepath, new_filepath)
        print(f"已將 '{filename}' 重命名為 '{new_filename}'")

    def rename_files_in_directory(self):
        """批次處理目錄中的所有檔案"""
        for filename in os.listdir(self.directory):
            old_filepath = os.path.join(self.directory, filename)
            if os.path.isfile(old_filepath):
                new_filename, new_filepath = self.generate_new_filename(filename)
                self.rename_file(old_filepath, new_filepath, filename, new_filename)

# modules/file_renaming.py
import os
from collections import defaultdict

class FileRenaming:
    @staticmethod
    def rename_files_in_directory(directory):
        """
        在指定目錄中重命名所有檔案，使檔名包含其副檔名類型和一個獨特的編號。
        Args:
            directory (str): 欲進行檔案重命名的目錄路徑。
        """
        extension_counts = defaultdict(int)

        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)
            if os.path.isfile(filepath):
                file_extension = os.path.splitext(filename)[1].lower()
                extension_counts[file_extension] += 1
                new_filename = f"{file_extension[1:]}_{extension_counts[file_extension]}{file_extension}"
                new_filepath = os.path.join(directory, new_filename)

                counter = 1
                while os.path.exists(new_filepath):
                    new_filename = f"{file_extension[1:]}_{extension_counts[file_extension]}_{counter}{file_extension}"
                    new_filepath = os.path.join(directory, new_filename)
                    counter += 1

                os.rename(filepath, new_filepath)
                print(f"已將 '{filename}' 重命名為 '{new_filename}'")
