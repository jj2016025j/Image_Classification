# 解壓縮 移除資料夾
import os
import shutil
import zipfile
import logging

# 設定日誌記錄，用於捕捉錯誤
logging.basicConfig(filename='error_log.txt', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')

def extract_and_clean_directory(src_dir):
    """
    解壓縮指定目錄下的所有.zip檔案，並清理原始資料夾結構。
    Args:
        src_dir (str): 源目錄路徑。
    """

    # 遍歷源目錄，解壓縮.zip檔案並處理錯誤
    for root, dirs, files in os.walk(src_dir):
        for name in files:
            if name.endswith('.zip'):
                zip_path = os.path.join(root, name)
                try:
                    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                        zip_ref.extractall(root)
                    os.remove(zip_path)  # 解壓縮後刪除.zip檔案
                except Exception as e:
                    logging.error(f"解壓縮 {zip_path} 時出錯: {e}")

    # 移動檔案、必要時重命名，並移除資料夾
    for root, dirs, files in os.walk(src_dir, topdown=False):
        for file in files:
            source_file_path = os.path.join(root, file)
            target_file_path = os.path.join(src_dir, file)

            # 如果目標檔案已存在，則重命名
            file_base, file_extension = os.path.splitext(file)
            i = 1
            while os.path.exists(target_file_path):
                target_file_path = os.path.join(src_dir, f"{file_base}_{i}{file_extension}")
                i += 1

            # 移動檔案並處理錯誤
            try:
                shutil.move(source_file_path, target_file_path)
            except Exception as e:
                logging.error(f"移動 {source_file_path} 到 {target_file_path} 時出錯: {e}")

        # 移除資料夾並處理錯誤
        for name in dirs:
            dir_path = os.path.join(root, name)
            try:
                if not os.listdir(dir_path):
                    os.rmdir(dir_path)
                else:
                    # 如果資料夾不為空，移動剩餘檔案
                    for remaining_file in os.listdir(dir_path):
                        remaining_file_path = os.path.join(dir_path, remaining_file)
                        remaining_target_path = os.path.join(src_dir, remaining_file)
                        shutil.move(remaining_file_path, remaining_target_path)
                    os.rmdir(dir_path)  # 現在資料夾應該為空，可以刪除
            except Exception as e:
                logging.error(f"移除資料夾 {dir_path} 時出錯: {e}")

# 使用範例，請替換成您的源目錄
source_directory = "C:/Users/User/Desktop/tablecloth/classification"  # 替換為您的源目錄路徑
extract_and_clean_directory(source_directory)
