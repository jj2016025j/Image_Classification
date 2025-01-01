# utils/image_operations.py

import re
import numpy as np
from PIL import Image, UnidentifiedImageError

def load_image(image_path, use_opencv=False):
    """
    加載圖像並選擇是否使用 OpenCV 處理。
    Args:
        image_path (str): 圖像路徑
        use_opencv (bool): 是否使用 OpenCV 加載並轉換圖像
    Returns:
        PIL.Image 或 None: 加載的圖像
    """
    try:
        if use_opencv:
            import cv2
            image = cv2.imread(image_path)
            if image is None:
                raise FileNotFoundError(f"Image not found: {image_path}")
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(image)
            print(image)
            return image
        else:
            img = Image.open(image_path)
            img.load()  # 確保圖像完全加載到內存
            print(img)
            return img
    except Exception as e:
        print(f"Error loading image: {e}")
        return None

def get_basic_image_details(img=None,image_path=None):
    """
    Args:
        獲取圖片的基本資訊(要先經由Image.open及load)
        只能處理這種圖像<PIL.PngImagePlugin.PngImageFile image mode=RGB size=1024x1536 at 0x2937F360C90>
    Returns:
        format: 'PNG'       # 圖片格式
        mode: 'RGB'         # 圖片模式
        size: (1024, 1536)  # 圖片大小
        info: {}            # 其他資訊

    """
    if img is None:
        if image_path is None:
            return None
        img = Image.open(image_path)
        img.load()
        return img

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
        # "info": info           # 其他資訊
        "info": img.info        # 其他資訊
        
    }

def convert_image_to_array(img):
    """
    將圖片轉換為numpy陣列來訪問像素數據
    """
    if img is None:
        return None
    return np.array(img)

def get_model_name_from_image_info(info):
    """從圖片的metadata中提取模型名稱"""
    try:
        img_info_str = str(info)
        model_index = img_info_str.find('Model:')
        if model_index != -1:
            return img_info_str[model_index:].split(',')[0].strip().replace("Model: ", "")
        else:
            return None
    except (OSError, UnidentifiedImageError):
        return None

def parse_image_parameters(info):
    """
    从图像的metadata中提取所有相关参数，支持复杂参数解析
    Args:
        info (dict): 图像的info元数据
    Returns:
        dict: 提取的参数字典
    """
    parameters_dict = {}
    if 'parameters' in info:
        parameters = info['parameters']

        # 使用正则表达式匹配键值对，包括括号和其他复杂格式
        param_matches = re.findall(r'([\w\s<>:]+):\s*([^,\n]+)', parameters)
        for key, value in param_matches:
            cleaned_key = re.sub(r'[()<>]', '', key.strip())
            cleaned_value = re.sub(r'[()<>]', '', value.strip())

            # 如果是Lora或类似格式，分离为更简洁的键值对
            if ":" in cleaned_key:
                lora_key, lora_value = cleaned_key.split(":", 1)
                parameters_dict[lora_key.strip()] = lora_value.strip()
            else:
                parameters_dict[cleaned_key] = cleaned_value

    return parameters_dict