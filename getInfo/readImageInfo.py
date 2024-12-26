import os
import shutil
from PIL import Image
import numpy as np
import json

def get_all_files_in_directory(directory_path):
    """
    獲取資料夾內所有檔案的路徑
    """
    all_files = []
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            all_files.append(file_path)
    return all_files

def load_image(image_path):
    """
    載入圖片並返回圖片對象
    """
    try:
        img = Image.open(image_path)
        img.close()  # 確保圖片文件被關閉
        return img
    except Exception as e:
        print(f"Error loading image(載入圖片時出錯): {e}")
        return None
def get_basic_image_details(img):
    """
    獲取圖片的基本資訊
    """
    if img is None:
        return None

    # 處理 img.info 中的 bytes 類型數據
    info = {}
    for key, value in img.info.items():
        if isinstance(value, bytes):
            info[key] = value.decode('utf-8', errors='ignore')
        else:
            info[key] = value

    return {
        "format": img.format,  # 圖片格式
        "mode": img.mode,      # 圖片模式
        "size": img.size,      # 圖片大小
        "info": info           # 其他資訊
    }


def convert_image_to_array(img):
    """
    將圖片轉換為numpy陣列來訪問像素數據
    """
    if img is None:
        return None
    return np.array(img)

def print_image_details(image_details):
    """
    打印圖片的基本資訊
    """
    if image_details is None:
        print("No image details to display.(無法顯示圖片資訊。)")
        return
    print("Basic Image Details(圖片基本資訊):")
    for key, value in image_details.items():
        print(f"{key}: {value}")

def print_pixel_data(image_array):
    """
    打印像素數據資訊
    """
    if image_array is None:
        print("No pixel data to display.(無法顯示像素數據。)")
        return
    print("\nPixel Data(像素數據資訊):")
    print(f"Type of the image array(數據類型): {image_array.dtype}")
    print(f"Shape of the image array(數據形狀): {image_array.shape}")

def get_image_basic_details(image_path):
    """
    獲取圖片的基本資訊
    """
    img = load_image(image_path)
    image_details = get_basic_image_details(img)
    print_image_details(image_details)
    return image_details

def get_image_pixel_data(image_path):
    """
    獲取圖片的像素數據
    """
    img = load_image(image_path)
    image_array = convert_image_to_array(img)
    print_pixel_data(image_array)
    return image_array

def image_details_to_json(image_details):
    """
    將圖片基本資訊轉換為JSON格式
    """
    if image_details is None:
        return "{}"
    return json.dumps(image_details, indent=4)

def save_json_to_file(json_data, file_path):
    """
    將JSON數據保存到文件
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(json_data)
        print(f"JSON data saved to(JSON數據已保存到) {file_path}")
    except Exception as e:
        print(f"Error saving JSON to file(保存JSON文件時出錯): {e}")

def contains_any_key(info, keys):
    """
    檢查 info 中是否包含指定的鍵名稱
    """
    return any(key in info for key in keys)

def filter_and_move_images(directory_path, matched_directory, unmatched_directory, keys):
    """
    篩選圖片並移動到不同的資料夾
    """
    all_files = get_all_files_in_directory(directory_path)
    for file_path in all_files:
        if file_path.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif')):
            img = load_image(file_path)
            if img:
                details = get_basic_image_details(img)
                if details and contains_any_key(details['info'], keys):
                    print(f"移動文件到 {matched_directory}: {file_path}")
                    shutil.move(file_path, os.path.join(matched_directory, os.path.basename(file_path)))
                else:
                    print(f"移動文件到 {unmatched_directory}: {file_path}")
                    shutil.move(file_path, os.path.join(unmatched_directory, os.path.basename(file_path)))
            
if __name__ == "__main__":
    image_directory_path = r'C:\Users\User\Downloads\sd圖片'  # 替換為你的圖片資料夾路徑
    matched_directory = r'C:\Users\User\Downloads\sd圖片'  # 替換為符合條件的圖片資料夾路徑
    unmatched_directory = r'C:\Users\User\Desktop\tablecloth\沒參數'  # 替換為不符合條件的圖片資料夾路徑
    
    os.makedirs(matched_directory, exist_ok=True)
    os.makedirs(unmatched_directory, exist_ok=True)
    
    keys = [
        'parameters',
        'Negative prompt',
        'Steps',
        'Sampler',
        'CFG scale',
        'Seed',
        'Size',
        'Model hash',
        'Model',
        'Denoising strength',
        'Hires upscale',
        'Hires steps',
        'Hires upscaler'
    ]  # 替換為你想要篩選的鍵名稱
    
    filter_and_move_images(image_directory_path, matched_directory, unmatched_directory, keys)

from PIL import Image, UnidentifiedImageError

def get_model_name_from_image(image_path):
    """從圖片的metadata中提取模型名稱"""
    try:
        with Image.open(image_path) as img:
            img_info_str = str(img.info)
            model_index = img_info_str.find('Model:')
            if model_index != -1:
                return img_info_str[model_index:].split(',')[0].strip().replace("Model: ", "")
            else:
                return None
    except (OSError, UnidentifiedImageError):
        return None