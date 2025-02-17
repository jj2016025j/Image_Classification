import os
import shutil

class FileOperations:
    """通用檔案管理工具"""

    @staticmethod
    def create_directory(directory_path):
        """建立資料夾（若不存在則創建）"""
        os.makedirs(directory_path, exist_ok=True)

    @staticmethod
    def move_file(source_path, destination_path):
        """ 移動檔案 """
        try:
            shutil.move(source_path, destination_path)
            print(f"檔案已移動到 {destination_path}")
        except Exception as e:
            print(f"無法移動檔案: {e}")
            
    @staticmethod
    def move_file(source_path, destination_path, filename=None):
        """移動檔案到指定目錄，處理重名問題"""
        FileOperations.create_directory(destination_path)

        # 如果未提供檔名，則使用原始名稱
        target_filename = filename if filename else os.path.basename(source_path)
        target_path = os.path.join(destination_path, target_filename)

        counter = 1
        base_name, ext = os.path.splitext(target_filename)

        # 避免重名，添加額外數字
        while os.path.exists(target_path):
            target_filename = f"{base_name}_{counter}{ext}"
            target_path = os.path.join(destination_path, target_filename)
            counter += 1

        try:
            shutil.move(source_path, target_path)
            print(f"檔案已移動到 {target_path}")
            return target_path
        except Exception as e:
            print(f"無法移動檔案: {e}")

    @staticmethod
    def clean_empty_directories(directory):
        """遞迴刪除空目錄"""
        for root, dirs, _ in os.walk(directory, topdown=False):
            for dir_name in dirs:
                dir_path = os.path.join(root, dir_name)
                if not os.listdir(dir_path):
                    os.rmdir(dir_path)
                    print(f"刪除空目錄: {dir_path}")

    @staticmethod
    def get_all_files_in_directory(directory_path):
        """獲取資料夾內所有檔案的路徑"""
        return [os.path.join(root, file)
                for root, _, files in os.walk(directory_path)
                for file in files]

    @classmethod
    def resolve_duplicate_filename(cls, destination_path, filename):
        """
        檢查目標路徑是否已有相同檔名，若有則添加數字後綴。
        Args:
            destination_path (str): 目標資料夾
            filename (str): 原始檔名
        Returns:
            str: 變更後的新檔案名稱（若無重複則維持原始名稱）
        """
        target_path = os.path.join(destination_path, filename)
        base_name, ext = os.path.splitext(filename)
        counter = 1

        while os.path.exists(target_path):
            new_filename = f"{base_name}_{counter}{ext}"
            target_path = os.path.join(destination_path, new_filename)
            counter += 1

        return target_path

    @classmethod
    def move_file(cls, source_path, destination_path, filename=None, handle_duplicates=True):
        """
        移動檔案到指定目錄，並處理重名問題
        Args:
            source_path (str): 原始檔案路徑
            destination_path (str): 目標資料夾路徑
            filename (str, optional): 指定新檔名，若為 None 則保持原始名稱
            handle_duplicates (bool): 是否處理重名問題，預設為 True
        Returns:
            str: 移動後的檔案最終路徑
        """
        # 確保目標資料夾存在
        cls.create_directory(destination_path)

        # 如果未提供檔名，則使用原始名稱
        target_filename = filename if filename else os.path.basename(source_path)

        # 檢查是否需要處理重名問題
        if handle_duplicates:
            target_path = cls.resolve_duplicate_filename(destination_path, target_filename)
        else:
            target_path = os.path.join(destination_path, target_filename)

        try:
            shutil.move(source_path, target_path)
            print(f"✅ 檔案已移動到 {target_path}")
            return target_path
        except Exception as e:
            print(f"❌ 無法移動檔案: {e}")
            return None