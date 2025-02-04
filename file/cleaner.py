# modules/cleaner.py
import os
import shutil

class DirectoryCleaner:
    @staticmethod
    def clear_folder(folder_path):
        """
        清除目錄中的所有內容
        Args:
            folder_path (str): 目錄路徑
        """
        try:
            for filename in os.listdir(folder_path):
                file_path = os.path.join(folder_path, filename)
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.remove(file_path)
                    print(f"File {file_path} deleted successfully.")
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
                    print(f"Folder {file_path} deleted successfully.")
            print(f"Folder {folder_path} cleared successfully.")
        except FileNotFoundError:
            print(f"Error: The folder {folder_path} does not exist.")
        except PermissionError:
            print(f"Error: You do not have permission to clear {folder_path}.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
