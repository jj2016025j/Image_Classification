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
