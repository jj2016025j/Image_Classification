import os
import shutil

class DirectoryCleaner:
    """資料夾清理工具"""

    @staticmethod
    def clear_folder(folder_path):
        """
        清除指定資料夾內所有檔案和子目錄
        Args:
            folder_path (str): 目標資料夾路徑
        """
        try:
            for filename in os.listdir(folder_path):
                file_path = os.path.join(folder_path, filename)
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.remove(file_path)
                    print(f"已刪除檔案: {file_path}")
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
                    print(f"已刪除資料夾: {file_path}")
            print(f"資料夾 {folder_path} 清理完成。")
        except FileNotFoundError:
            print(f"錯誤: {folder_path} 不存在。")
        except PermissionError:
            print(f"錯誤: 無權限清理 {folder_path}。")
        except Exception as e:
            print(f"發生意外錯誤: {e}")
