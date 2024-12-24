### process_images.py
import os
import shutil

from classification.FileUtils import move_file_to_folder
from generated_images.get_model_name import get_model_name_from_image

def process_images(source_path, target_path):
    """處理圖片並按模型名稱分類"""
    count = 0

    # 確保目標資料夾存在
    if not os.path.exists(target_path):
        os.mkdir(target_path)
        
    for filename in os.listdir(source_path):
        source_file = os.path.join(source_path, filename)

        if filename.endswith((".png", ".jpg", ".jpeg")):
            model_name = get_model_name_from_image(source_file)
            if model_name:
                target_folder = os.path.join(target_path, model_name)
            else:
                target_folder = os.path.join(target_path, "other")

            if not os.path.exists(target_path):
                os.mkdir(target_path)
            shutil.move(source_file, os.path.join(target_folder, filename))
            print(f"Moved file {filename} to {target_folder}")
            count += 1
        else:
            print(f"Skipping file {filename}: Invalid image format")

    print(f"Processed {count} files.")