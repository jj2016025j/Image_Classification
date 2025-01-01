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

def weighted_sample(option_dict, count=1, mode='positive'):
    """
    根據權重隨機選擇不重複的項目，支持正面和負面提示詞。
    :param option_dict: 包含提示詞和正面/負面權重的字典。
    :param count: 選擇的項目數量。
    :param mode: 選擇模式，可為 'positive' 或 'negative'。
    :return: 選中的提示詞列表。
    :raises TypeError: 如果 option_dict 結構不符合預期。
    """
    # 檢查數據結構是否正確
    if not all(isinstance(value, dict) and mode in value for value in option_dict.values()):
        raise TypeError(
            f"Invalid option_dict structure. Each value must be a dictionary containing '{mode}' key."
        )

    keys = list(option_dict.keys())
    weights = [option_dict[key][mode] for key in keys]  # 根據模式選擇對應權重
    selected_items = []

    while len(selected_items) < min(count, len(keys)):
        choice = random.choices(population=keys, weights=weights, k=1)[0]
        if choice not in selected_items:
            selected_items.append(choice)

    # 返回選項（僅保留提示詞，不包含權重）
    return selected_items

def flatten_prompts(nested_list):
    """
    將嵌套的提示詞陣列展平為單一列表。
    :param nested_list: 包含嵌套陣列的列表。
    :return: 平坦化的字串提示詞列表。
    """
    flat_list = []

    def flatten(item):
        if isinstance(item, list):  # 如果是列表，遞歸展平
            for sub_item in item:
                flatten(sub_item)
        elif isinstance(item, tuple):  # 如果是元組，提取第一個元素
            flat_list.append(item[0])
        else:  # 如果是字串，直接添加
            flat_list.append(item)

    flatten(nested_list)
    return list(set(flat_list))  # 去重（如果不需要去重，移除 set 處理）