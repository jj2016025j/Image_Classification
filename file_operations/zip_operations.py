# modules/zip_operations.py
import os
import zipfile
import logging

class ZipOperations:
    @staticmethod
    def extract_zip_files(src_dir):
        """
        解壓縮指定目錄下的所有.zip檔案
        Args:
            src_dir (str): 源目錄路徑。
        """
        for root, dirs, files in os.walk(src_dir):
            for name in files:
                if name.endswith('.zip'):
                    zip_path = os.path.join(root, name)
                    try:
                        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                            zip_ref.extractall(root)
                        os.remove(zip_path)
                    except Exception as e:
                        logging.error(f"解壓縮 {zip_path} 時出錯: {e}")
