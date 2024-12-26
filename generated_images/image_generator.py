import base64
from io import BytesIO
import requests
from PIL import Image

from config.image import GENERATE_IMAGE_URL

def generate_images(generate_params, generate_image_url = GENERATE_IMAGE_URL):
    """
    使用 Stable Diffution txt_to_img 進行圖片生成
    """
    try:
        # 調用生成圖片的 API
        response = requests.post(generate_image_url, json=generate_params)

        # 檢查 HTTP 回應狀態碼
        if response.status_code != 200:
            print(f"Error generating image: {response.status_code}")
            raise Exception(f"HTTP Error {response.status_code}: {response.text}")
        
        # 解析回應，提取圖片數據
        images_base64 = response.json().get("images", [])
        images = [decode_base64_image(img) for img in images_base64]

        return images
    
    except Exception as e:
        print(f"Error generating image: {e}")
        return None, None

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
