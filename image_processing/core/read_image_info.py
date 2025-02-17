import json
from image_loader import load_image
from image_parser import get_basic_image_details, get_model_name_from_image_info, parse_image_parameters
from file_management.core.file_operations import create_directory, filter_and_move_images

if __name__ == "__main__":
    image_path = r'test2.png'  # 替換為你的圖片路徑
    matched_directory = r'C:\Users\User\Downloads\sd圖片'  # 符合條件的圖片資料夾
    unmatched_directory = r'C:\Users\User\Desktop\tablecloth\沒參數'  # 不符合條件的圖片資料夾

    img = load_image(image_path)
    if not img:
        exit()

    info = get_basic_image_details(img)
    print("圖片基本資訊:")
    print(json.dumps(info, indent=4, ensure_ascii=False))

    model_name = get_model_name_from_image_info(info)
    print(f"模型名稱: {model_name}")

    parameters_dict = parse_image_parameters(info.get('info', ''))
    print("解析後的參數:")
    print(json.dumps(parameters_dict, indent=4, ensure_ascii=False))

    model_name = parameters_dict.get('Model', 'No model name found')
    print(f"最終提取的模型名稱: {model_name}")

    # 建立資料夾
    create_directory(matched_directory)
    create_directory(unmatched_directory)

    # 定義篩選鍵值
    keys = [
        'parameters', 'Negative prompt', 'Steps', 'Sampler', 'CFG scale',
        'Seed', 'Size', 'Model hash', 'Model', 'Denoising strength',
        'Hires upscale', 'Hires steps', 'Hires upscaler'
    ]

    # 移動符合條件的圖片
    filter_and_move_images(image_path, matched_directory, unmatched_directory, keys)
