import os
from PIL import Image, UnidentifiedImageError
from dotenv import load_dotenv

from config.image import ASPECT_RATIO_THRESHOLD, LONG_EDGE_THRESHOLD, SHORT_EDGE_THRESHOLD, SOURCE_DIRECTORY, TARGET_DIRECTORY
from file_operations.file_operations import FileOperations

Image.MAX_IMAGE_PIXELS = 9999999999999

class WallpaperClassifier:
    def __init__(self, source_path, target_path, long_edge_threshold, short_edge_threshold, aspect_ratio_threshold):
        self.source_path = source_path
        self.target_path = target_path
        self.long_edge_threshold = long_edge_threshold
        self.short_edge_threshold = short_edge_threshold
        self.aspect_ratio_threshold = aspect_ratio_threshold
        
    def sanitize_filename(self, filename):
        """
        替換文件名中的特殊字符以避免不合法
        """
        return "".join(c if c.isalnum() or c in (" ", ".", "_") else "_" for c in filename)

    def classify_wallpaper(self, image_path):
        """
        根據圖片的較長邊、較短邊和寬高比例進行分類
        Args:
            image_path (str): 圖片文件路徑
        Returns:
            str: 目標資料夾名稱
        """
        try:
            with Image.open(image_path) as img:
                width, height = img.size
                larger, smaller = max(width, height), min(width, height)
                aspect_ratio = larger / smaller

                if aspect_ratio < self.aspect_ratio_threshold or aspect_ratio > 2:
                    return "others"

                if larger >= self.long_edge_threshold and smaller >= self.short_edge_threshold:
                    return "computer_wallpapers" if width > height else "mobile_wallpapers"
                return "others"
        except (OSError, UnidentifiedImageError):
            print(f"Skipped file {image_path}: Unidentified image format")
            return "others"

    def classify_images(self):
        """
        遍歷源目錄的圖片，根據分類結果進行文件移動
        """
        FileOperations.create_directory(self.target_path)
        count = 0

        for filename in os.listdir(self.source_path):
            file_path = os.path.join(self.source_path, filename)
            if not os.path.isfile(file_path):
                continue

            if filename.lower().endswith((".png", ".jpg", ".jpeg")):
                category = self.classify_wallpaper(file_path)
            else:
                print(f"Skipping file {filename}: Invalid format")
                continue

            category_path = os.path.join(self.target_path, category)
            FileOperations.create_directory(category_path)
            FileOperations.move_file(file_path, category_path, filename)
            count += 1

        print(f"Processed {count} files.")
        
def wallpaper_classifier_main():
    """
    主函數，用於執行圖片分類為桌布操作
    """
    # 加載環境變量
    print(SOURCE_DIRECTORY)
    print(TARGET_DIRECTORY)
    print(LONG_EDGE_THRESHOLD)
    print(SHORT_EDGE_THRESHOLD)
    print(ASPECT_RATIO_THRESHOLD)
    
    # 分類桌布圖片   
    wallpaper_classifier = WallpaperClassifier(
        SOURCE_DIRECTORY, 
        TARGET_DIRECTORY, 
        LONG_EDGE_THRESHOLD, 
        SHORT_EDGE_THRESHOLD, 
        ASPECT_RATIO_THRESHOLD
    )
    wallpaper_classifier.classify_images()
