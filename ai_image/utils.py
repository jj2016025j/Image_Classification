import base64
from io import BytesIO
from PIL import Image
    
import random

def decode_base64_image(base64_string):
    """
    將 Base64 字串轉換為 PIL 圖片對象
    """
    try:
        if "," in base64_string:
            base64_string = base64_string.split(",", 1)[1]
        image_data = BytesIO(base64.b64decode(base64_string))
        image = Image.open(image_data)
        return image
    except Exception as e:
        print(f"Error decoding image: {e}")
        return None

def weighted_sample(option_dict, count=1):
    """
    根據權重隨機選擇不重複的項目。
    :param option_dict: 包含提示詞和權重的字典。
    :param count: 選擇的項目數量。
    :return: 不重複選擇的項目列表。
    """
    keys = list(option_dict.keys())
    weights = list(option_dict.values())
    selected_items = []
    while len(selected_items) < min(count, len(keys)):
        choice = random.choices(population=keys, weights=weights, k=1)[0]
        if choice not in selected_items:
            selected_items.append(choice)
    return selected_items