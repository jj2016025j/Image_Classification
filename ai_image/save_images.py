import os
import base64
from io import BytesIO
from PIL import Image
import json
from PIL.PngImagePlugin import PngInfo
import traceback

from ai_image.config import OUTPUT_DIR

class ImageOperations:
    output_dir = OUTPUT_DIR
    @staticmethod
    def save_images(images, generate_params, filename_generator):
        """Save multiple images with metadata."""
        if not images:
            print("No images to save.")
            return

        os.makedirs(OUTPUT_DIR, exist_ok=True) 

        for img in images:
            try:
                image_filename = filename_generator(ImageOperations.output_dir)
                ImageOperations.save_image_with_metadata(img, generate_params, image_filename)
            except Exception as e:
                print(f"Error saving image: {e}")         

    @staticmethod
    def save_image_with_metadata(image_data, params, filename):
        """
        Save an image and embed generation parameters as metadata.
        """
        try:
            image = ImageOperations.convert_to_pil_image(image_data)
            image_with_metadata = ImageOperations.add_metadata_to_image(image, params)
            image_with_metadata.save(filename, format='PNG')
            print(f"Image saved as {filename}")
        except Exception as e:
            error_message = f"Error in save_image_with_metadata: {str(e)}\n"
            error_message += traceback.format_exc()
            print(error_message)
            
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
        params_json = json.dumps(params)
        # 將JSON字符串添加為元數據
        metadata.add_text("Generation Parameters", params_json)
        
        # 創建一個新的圖片對象，包含原圖像數據和新的元數據
        new_image = Image.new(image.mode, image.size)
        new_image.putdata(list(image.getdata()))
        new_image.info["parameters"] = params_json
        
        return new_image
