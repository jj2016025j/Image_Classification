import base64
from io import BytesIO
from PIL import Image

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