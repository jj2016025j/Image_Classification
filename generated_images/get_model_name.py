### get_model_name.py
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