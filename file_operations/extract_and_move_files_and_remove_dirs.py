import os
import shutil
import zipfile
import logging

# 設定日誌記錄，用於捕捉錯誤
logging.basicConfig(filename='error_log.txt', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')

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
                    os.remove(zip_path)  # 解壓縮後刪除.zip檔案
                except Exception as e:
                    logging.error(f"解壓縮 {zip_path} 時出錯: {e}")

def move_files(src_dir, dst_dir):
    """
    移動檔案到目標目錄並確保文件名唯一
    Args:
        src_dir (str): 源目錄路徑。
        dst_dir (str): 目標目錄路徑。
    """
    for root, dirs, files in os.walk(src_dir, topdown=False):
        for file in files:
            source_file_path = os.path.join(root, file)
            target_file_path = os.path.join(dst_dir, file)

            # 如果目標檔案已存在，則重命名
            file_base, file_extension = os.path.splitext(file)
            i = 1
            while os.path.exists(target_file_path):
                target_file_path = os.path.join(dst_dir, f"{file_base}_{i}{file_extension}")
                i += 1

            try:
                shutil.move(source_file_path, target_file_path)
            except Exception as e:
                logging.error(f"移動 {source_file_path} 到 {target_file_path} 時出錯: {e}")

def clean_empty_directories(src_dir):
    """
    清理空資料夾
    Args:
        src_dir (str): 源目錄路徑。
    """
    for root, dirs, files in os.walk(src_dir, topdown=False):
        for name in dirs:
            dir_path = os.path.join(root, name)
            try:
                if not os.listdir(dir_path):
                    os.rmdir(dir_path)
            except Exception as e:
                logging.error(f"移除資料夾 {dir_path} 時出錯: {e}")

def extract_and_clean_directory(src_dir, dst_dir=None):
    """
    解壓縮指定目錄下的所有.zip檔案，並清理原始資料夾結構。
    Args:
        src_dir (str): 源目錄路徑。
        dst_dir (str): 目標目錄路徑，如果未指定，則使用源目錄。
    """
    if dst_dir is None:
        dst_dir = src_dir

    extract_zip_files(src_dir)
    move_files(src_dir, dst_dir)
    clean_empty_directories(src_dir)

# 使用範例，請替換成您的源目錄
source_directory = "C:/Users/User/GitHub/ImageClassification/test"  # 替換為您的源目錄路徑
destination_directory = "C:/Users/User/GitHub/ImageClassification/test"

extract_and_clean_directory(source_directory, destination_directory)

