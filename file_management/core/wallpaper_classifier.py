import os
from PIL import Image, UnidentifiedImageError
from file_management.core.file_operations import FileOperations
from file_management.config.image_config import ASPECT_RATIO_THRESHOLD, LONG_EDGE_THRESHOLD, SHORT_EDGE_THRESHOLD, SOURCE_DIRECTORY, TARGET_DIRECTORY

Image.MAX_IMAGE_PIXELS = 9999999999999  # 允許大圖片處理

class WallpaperClassifier:
    """桌布圖片分類工具"""

    def __init__(self, source_path, target_path, long_edge_threshold, short_edge_threshold, aspect_ratio_threshold):
        self.source_path = source_path
        self.target_path = target_path
        self.long_edge_threshold = long_edge_threshold
        self.short_edge_threshold = short_edge_threshold
        self.aspect_ratio_threshold = aspect_ratio_threshold

    @staticmethod
    def sanitize_filename(filename):
        """過濾不合法的文件名字符"""
        return "".join(c if c.isalnum() or c in (" ", ".", "_") else "_" for c in filename)

    def classify_wallpaper(self, image_path):
        """
        根據圖片尺寸和比例進行分類
        Args:
            image_path (str): 圖片文件路徑
        Returns:
            str: 分類資料夾名稱
        """
        try:
            with Image.open(image_path) as img:
                width, height = img.size
                larger, smaller = max(width, height), min(width, height)
                aspect_ratio = larger / smaller

                if aspect_ratio < self.aspect_ratio_threshold or aspect_ratio > 2:
                    return "others"

                return "computer_wallpapers" if width > height else "mobile_wallpapers"
        except (OSError, UnidentifiedImageError):
            print(f"跳過文件 {image_path}: 非圖片格式")
            return "others"

    def classify_images(self):
        """處理資料夾內所有圖片並分類"""
        FileOperations.create_directory(self.target_path)
        count = 0

        for filename in os.listdir(self.source_path):
            file_path = os.path.join(self.source_path, filename)
            if not os.path.isfile(file_path):
                continue

            if filename.lower().endswith((".png", ".jpg", ".jpeg")):
                category = self.classify_wallpaper(file_path)
            else:
                print(f"跳過文件 {filename}: 非圖片格式")
                continue

            category_path = os.path.join(self.target_path, category)
            FileOperations.create_directory(category_path)
            FileOperations.move_file(file_path, category_path, filename)
            count += 1

        print(f"已處理 {count} 個文件。")


def wallpaper_classifier_main():
    """主函數，用於分類桌布圖片"""
    classifier = WallpaperClassifier(
        SOURCE_DIRECTORY,
        TARGET_DIRECTORY,
        LONG_EDGE_THRESHOLD,
        SHORT_EDGE_THRESHOLD,
        ASPECT_RATIO_THRESHOLD
    )
    classifier.classify_images()
