import os
import zipfile
import logging

class ZipOperations:
    """ZIP 檔案管理工具"""

    @staticmethod
    def extract_zip_files(src_dir):
        """
        解壓縮目錄下的所有 .zip 檔案
        Args:
            src_dir (str): 來源資料夾
        """
        for root, _, files in os.walk(src_dir):
            for name in files:
                if name.endswith('.zip'):
                    zip_path = os.path.join(root, name)
                    try:
                        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                            zip_ref.extractall(root)
                        os.remove(zip_path)
                        print(f"已解壓並刪除 {zip_path}")
                    except Exception as e:
                        logging.error(f"解壓縮 {zip_path} 時發生錯誤: {e}")
