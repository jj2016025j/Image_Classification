import os
import shutil
from PIL import Image

def get_resolution(image_path):
    """
    獲取圖片的解析度
    """
    with Image.open(image_path) as im:
        width, height = im.size
    return (width, height)

def classify_by_resolution(width, height):
    """
    根據圖片解析度分類圖片，並返回目標子目錄名稱
    """
    if width * height >= 7680 * 4320:
        return "4320P (UHD 8K)"
    elif width * height >= 3840 * 2160:
        return "2160P (UHD 4K)"
    elif width * height >= 1920 * 1080:
        return "1080P (Full HD)"
    elif width * height >= 1280 * 720:
        return "720P (HD)"
    elif width * height >= 640 * 480:
        return "480P (SD)"
    else:
        return "low_resolution"

def classify_image(image_path):
    """
    根據圖片的解析度和寬高比例分類圖片，並返回目標子目錄名稱
    """
    try:
        width, height = get_resolution(image_path)
        aspect_ratio = width / height

        # 如果寬高相差過大，放到其他分類
        if aspect_ratio > 2 or aspect_ratio < 0.5:
            return "other"
        
        return classify_by_resolution(width, height)
    except Exception:
        return "other"
  
def classify_by_extension(extension):
    """
    根據文件擴展名分類文件
    """
    if extension in [".jpg", ".jpeg", ".png"]:
        return "images"
    elif extension == ".gif":
        return "gif"
    elif extension == ".mp4":
        return "video"
    else:
        return "other"

def classify(image_path, extension):
    """
    根據文件類型和解析度分類文件，並返回目標子目錄名稱
    """
    if extension in [".jpg", ".jpeg", ".png"]:
        return classify_image(image_path)
    else:
        return classify_by_extension(extension)
          
def move_file(source_file, target_dir, image_name):
    """
    移動檔案到目標目錄，並處理重名問題
    """
    target_path = os.path.join(target_dir, image_name)
    base_name, ext = os.path.splitext(image_name)
    i = 1

    while os.path.exists(target_path):
        target_path = os.path.join(target_dir, f"{base_name}_{i}{ext}")
        i += 1

    shutil.move(source_file, target_path)
    return target_path

def copy_file(source_file, target_dir, image_name):
    """
    複製檔案到目標目錄，並處理重名問題
    """
    target_path = os.path.join(target_dir, image_name)
    base_name, ext = os.path.splitext(image_name)
    i = 1

    while os.path.exists(target_path):
        target_path = os.path.join(target_dir, f"{base_name}_{i}{ext}")
        i += 1

    shutil.copy(source_file, target_path)
    return target_path

def process_files(source_directory, target_directory):
    """
    處理源目錄中的所有文件，並根據分類結果移動或複製到目標目錄
    """
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    stats = {
        "same_drive_move": 0,
        "same_drive_replace": 0,
        "different_drive_move": 0,
        "different_drive_replace": 0
    }

    for root, dirs, files in os.walk(source_directory):
        for image_name in files:
            image_path = os.path.join(root, image_name)
            extension = os.path.splitext(image_path)[1]
            target_subdir = classify(image_path, extension)
            target_subdir_path = os.path.join(target_directory, target_subdir)

            if not os.path.exists(target_subdir_path):
                os.makedirs(target_subdir_path)

            same_drive = os.stat(source_directory).st_dev == os.stat(target_directory).st_dev

            if same_drive:
                try:
                    new_path = move_file(image_path, target_subdir_path, image_name)
                    stats["same_drive_move"] += 1
                except FileExistsError:
                    os.remove(new_path)
                    new_path = move_file(image_path, target_subdir_path, image_name)
                    stats["same_drive_replace"] += 1
            else:
                try:
                    new_path = copy_file(image_path, target_subdir_path, image_name)
                    os.remove(image_path)
                    stats["different_drive_move"] += 1
                except FileExistsError:
                    os.remove(new_path)
                    new_path = copy_file(image_path, target_subdir_path, image_name)
                    os.remove(image_path)
                    stats["different_drive_replace"] += 1

        # 刪除空目錄
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            if not os.listdir(dir_path):
                os.rmdir(dir_path)

    print_stats(stats)

def print_stats(stats):
    """
    打印統計數據
    """
    print(f"同硬碟移動: {stats['same_drive_move']}")
    print(f"同硬碟取代: {stats['same_drive_replace']}")
    print(f"不同硬碟移動: {stats['different_drive_move']}")
    print(f"不同硬碟取代: {stats['different_drive_replace']}")

if __name__ == "__main__":
    source_directory = "C:/Users/User/GitHub/ImageClassification/test"
    target_directory = "C:/Users/User/GitHub/ImageClassification/test"
    process_files(source_directory, target_directory)
