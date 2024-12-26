from datetime import datetime
import uuid
import os
import base64
from io import BytesIO
from PIL import Image
import json
from PIL.PngImagePlugin import PngInfo
import traceback

from config.image import OUTPUT_DIR

class ImageOperations:
    @staticmethod
    def generate_uuid4_based_image_filename(output_dir):
        """
        生成 uuid4 唯一的圖片檔案名。
        Args:
        output_dir: 輸出目錄的路徑
        Returns:
        完整的圖片檔案路徑
        """
        output_filename = os.path.join(output_dir, f"image_{uuid.uuid4().hex}.png")
        return output_filename

    @staticmethod
    def generate_time_based_image_filename():
        """
        生成基於 當前時間 的唯一圖片檔案名。
        Args:
        output_dir: 輸出目錄的路徑
        Returns:
        完整的圖片檔案路徑
        """
        current_time = datetime.now()
        time_string = current_time.strftime("%Y%m%d_%H%M%S_%f")
        filename = f"image_{time_string}.png"
                
        os.makedirs(OUTPUT_DIR, exist_ok=True) 
        output_filename = os.path.join(OUTPUT_DIR, filename)
    
        return output_filename

    @staticmethod
    def save_images(images, generate_params):
        """保存多張生成的圖片。"""
        if not images:
            print("No images to save.")
            return

        os.makedirs(OUTPUT_DIR, exist_ok=True) 

        for i, img in enumerate(images):
            image_filename = ImageOperations.generate_time_based_image_filename()
            ImageOperations.save_image_with_metadata(img, generate_params)             

    @staticmethod
    def convert_to_pil_image(image_data):
        """
        將不同格式的圖片數據轉換為PIL Image對象。
        
        Args:
        image_data: 圖片數據（可能是Base64編碼、二進制數據或PIL Image對象）
        
        Returns:
        PIL Image對象
        """
        if isinstance(image_data, Image.Image):
            return image_data
        
        if isinstance(image_data, str):
            # 處理Base64編碼的圖片
            if "," in image_data:
                image_data = image_data.split(",", 1)[1]
            image_data = base64.b64decode(image_data)
        
        # 處理二進制數據
        image = Image.open(BytesIO(image_data))
        
        return image

    @staticmethod
    def add_metadata_to_image(image, params):
        """
        將生成參數作為元數據添加到圖片中。
        
        Args:
        image: PIL Image對象
        params: 包含生成參數的字典
        
        Returns:
        添加了元數據的PIL Image對象
        """
        metadata = PngInfo()
        
        # 將params字典轉換為JSON字符串
        params_json = json.dumps(params)
        
        # 將JSON字符串添加為元數據
        metadata.add_text("Generation Parameters", params_json)
        
        # 創建一個新的圖片對象，包含原圖像數據和新的元數據
        new_image = Image.new(image.mode, image.size)
        new_image.putdata(list(image.getdata()))
        new_image.info["parameters"] = params_json
        
        return new_image
    
    @staticmethod
    def save_image_with_metadata(image_data, params):
        """
        根據圖片數據格式保存圖片，並添加元數據。
        
        Args:
        image_data: 圖片數據（可能是Base64編碼或二進制數據）
        filename: 保存的檔案名
        params: 生成圖片時使用的參數，可用於添加元數據
        """
        try:
            # 將image_data轉換為PIL Image對象
            image = ImageOperations.convert_to_pil_image(image_data)
            
            # 添加元數據（如果需要）
            image_with_metadata = ImageOperations.add_metadata_to_image(image, params)
            
            # 保存圖片
            image_filename = ImageOperations.generate_time_based_image_filename()
            image_with_metadata.save(image_filename, format='PNG')
            print(f"Image saved as {image_filename}")
        except Exception as e:
            error_message = f"Error in save_image_with_metadata : {str(e)}\n"
            error_message += traceback.format_exc()
            print(error_message)   