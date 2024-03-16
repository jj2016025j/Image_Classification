# 可以讀圖片資訊 ok 但是不是json格式 可以之後改
from PIL import Image
import numpy as np

def get_image_details(image_path):
    # 載入圖片
    with Image.open(image_path) as img:
        # 基本資訊
        image_details = {
            "format": img.format,  # 圖片格式
            "mode": img.mode,      # 圖片模式
            "size": img.size,      # 圖片大小
            "info": img.info       # 其他資訊
        }
    
    # 將圖片轉換為numpy陣列來訪問像素數據
    image_array = np.array(Image.open(image_path))

    # 打印基本資訊
    print("Basic Image Details:")
    for key, value in image_details.items():
        print(f"{key}: {value}")
    
    # 打印像素數據資訊
    print("\nPixel Data:")
    print(f"Type of the image array: {image_array.dtype}")
    print(f"Shape of the image array: {image_array.shape}")
    
    return image_details, image_array

# 使用函數在上傳的圖片上
image_path = 'example.png'
details, pixels = get_image_details(image_path)
