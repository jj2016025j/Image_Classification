# main.py
import json
import os
from getInfo.image_operations import get_basic_image_details, get_model_name_from_image_info, load_image, parse_image_parameters


if __name__ == "__main__":
    image_path = r'test2.png'  # 替換為你的圖片資料夾路徑
    # matched_directory = r'C:\Users\User\Downloads\sd圖片'  # 替換為符合條件的圖片資料夾路徑
    # unmatched_directory = r'C:\Users\User\Desktop\tablecloth\沒參數'  # 替換為不符合條件的圖片資料夾路徑

    img=load_image(image_path) 
    info = get_basic_image_details(img) 
    print(info)
    model_name = get_model_name_from_image_info(info)
    print(model_name)
    
    # 打印完整的字典 解析前打印 因為格式有錯誤所以會有問題
    print("Image Info:")
    print(json.dumps(info, indent=4, ensure_ascii=False))

    # 提取並打印解析後的參數 解析後打印問題比較少 但還是有
    parameters_dict = parse_image_parameters(info['info'])
    print("Parsed Parameters:")
    print(json.dumps(parameters_dict, indent=4, ensure_ascii=False))

    # 提取 Model 在這裡提取才有沒法提取
    model_name = parameters_dict.get('Model', 'No model name found')
    print(f"Model Name: {model_name}")
    
    
    load_image(image_path, True)
    # os.makedirs(matched_directory, exist_ok=True)
    # os.makedirs(unmatched_directory, exist_ok=True)

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

    # filter_and_move_images(image_path, matched_directory, unmatched_directory, keys)


