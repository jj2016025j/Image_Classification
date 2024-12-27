import requests

from ai_image.config import GENERATE_IMAGE_URL
from ai_image.utils import decode_base64_image

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

