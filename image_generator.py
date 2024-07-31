# import requests
# import json
# import base64
# import os

# # WebUI API的URL
# model_list_url = "http://127.0.0.1:7860/sdapi/v1/sd-models"
# generate_image_url = "http://127.0.0.1:7860/sdapi/v1/txt2img"

# # 生成圖片的參數
# generate_params = {
#     "prompt": "best quality, masterpiece, 8k, 1 girl, mane, multicolored hair",
#     "negative_prompt": "easynegative, nude, low quality, worst quality",
#     "steps": 20,
#     "cfg_scale": 8,
#     "width": 512,
#     "height": 512,
#     "restore_faces": True,
#     "tiling": False,
#     "do_not_save_samples": False,
#     "do_not_save_grid": False,
#     "enable_hr": True,
#     "hr_scale": 2,
#     "hr_upscaler": "ESRGAN_4x",
#     "hr_second_pass_steps": 20
# }

# # 獲取可用模型列表
# response = requests.get(model_list_url)

# if response.status_code != 200:
#     print("Failed to retrieve models")
#     exit()

# models = response.json()

# # 創建輸出目錄
# output_dir = "generated_images"
# os.makedirs(output_dir, exist_ok=True)

# # 遍歷每個模型並生成圖片
# for model in models:
#     model_name = model["model_name"]
#     print(f"Generating image with model: {model_name}")

#     # 更新生成圖片的參數，指定使用的模型
#     generate_params["override_settings"] = {"sd_model_checkpoint": model_name}
    
#     response = requests.post(generate_image_url, json=generate_params)
    
#     if response.status_code == 200:
#         data = response.json()
#         images = data.get("images", [])
        
#         for i, img in enumerate(images):
#             image_data = base64.b64decode(img.split(",", 1)[1])
#             image_filename = os.path.join(output_dir, f"{model_name}_{i}.png")
#             with open(image_filename, "wb") as f:
#                 f.write(image_data)
#         print(f"Image generated and saved for model: {model_name}")
#     else:
#         print(f"Error with model {model_name}: {response.status_code}")

# print("Done generating images with all models.")

import json
import requests
import base64
import os
from PIL import Image
from io import BytesIO

GENERATE_IMAGE_URL = "http://127.0.0.1:7860/sdapi/v1/txt2img"

def generate_image_test(model_name):
    """
    模擬圖片生成邏輯，返回 PIL Image 對象的列表
    """
    try:
        # 模擬生成圖片
        images = [Image.new('RGB', (512, 512), color='red') for _ in range(1)]
        return images
    except Exception as e:
        print(f"Error generating image with model {model_name}: {e}")
        return []

def generate_image(model_name, params):
    params["override_settings"] = {"sd_model_checkpoint": model_name}
    response = requests.post(GENERATE_IMAGE_URL, json=params)
    if response.status_code != 200:
        raise Exception(f"Error with model {model_name}: {response.status_code}")
    return response.json().get("images", [])
    
def save_image_with_metadata(image_data, filename, params):
    # 將 base64 編碼的字符串轉換為 PIL Image 對象
    if "," in image_data:
        image_data = base64.b64decode(image_data.split(",", 1)[1])
    else:
        image_data = base64.b64decode(image_data)
    image = Image.open(BytesIO(image_data))
    # metadata = json.dumps(params)
    # image.save(filename, format='PNG', pnginfo=Image.PngInfo(metadata=metadata))
    image.save(filename, format='PNG')
    # with open(filename, "wb") as f:
    #     f.write(base64.b64decode(image_data.split(",", 1)[1]))

def ensure_output_dir(output_dir):
    os.makedirs(output_dir, exist_ok=True)
