from PIL import Image
import numpy as np
import json

def load_image(image_path):
    """
    載入圖片並返回圖片對象
    """
    try:
        img = Image.open(image_path)
        return img
    except Exception as e:
        print(f"Error loading image: {e}")
        return None

def get_basic_image_details(img):
    """
    獲取圖片的基本資訊
    """
    if img is None:
        return None
    return {
        "format": img.format,  # 圖片格式
        "mode": img.mode,      # 圖片模式
        "size": img.size,      # 圖片大小
        "info": img.info       # 其他資訊
    }

def convert_image_to_array(img):
    """
    將圖片轉換為numpy陣列來訪問像素數據
    """
    if img is None:
        return None
    return np.array(img)

def print_image_details(image_details):
    """
    打印圖片的基本資訊
    """
    if image_details is None:
        print("No image details to display.")
        return
    print("Basic Image Details:")
    for key, value in image_details.items():
        print(f"{key}: {value}")

def print_pixel_data(image_array):
    """
    打印像素數據資訊
    """
    if image_array is None:
        print("No pixel data to display.")
        return
    print("\nPixel Data:")
    print(f"Type of the image array: {image_array.dtype}")
    print(f"Shape of the image array: {image_array.shape}")

def get_image_details(image_path):
    """
    獲取圖片的基本資訊和像素數據
    """
    img = load_image(image_path)
    image_details = get_basic_image_details(img)
    image_array = convert_image_to_array(img)
    print_image_details(image_details)
    print_pixel_data(image_array)
    return image_details, image_array

def image_details_to_json(image_details):
    """
    將圖片基本資訊轉換為JSON格式
    """
    if image_details is None:
        return "{}"
    return json.dumps(image_details, indent=4)

# 使用函數在上傳的圖片上
image_path = './src/example.png'
details, pixels = get_image_details(image_path)
json_details = image_details_to_json(details)

# 打印JSON格式的圖片基本資訊
print("\nImage Details in JSON format:")
print(json_details)
