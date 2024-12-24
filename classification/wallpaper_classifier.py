import os
from PIL import Image, UnidentifiedImageError
from prompt.prompt import FileUtils

# 设置 Image.MAX_IMAGE_PIXELS 以避免 DecompressionBombError
# Image.MAX_IMAGE_PIXELS = None
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
        替换文件名中的特殊字符
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
                # 判斷較大和較小的值，計算比例
                larger, smaller = max(width, height), min(width, height)
                aspect_ratio = larger / smaller

                if aspect_ratio < self.aspect_ratio_threshold or aspect_ratio > 2:
                    return "others"

                computer_wallpaper = larger >= self.long_edge_threshold and smaller >= self.short_edge_threshold
                mobile_wallpaper = smaller >= self.short_edge_threshold and aspect_ratio >= self.aspect_ratio_threshold

                if computer_wallpaper and width > height:
                    return "computer_wallpapers"
                elif mobile_wallpaper and height > width:
                    return "mobile_wallpapers"
                else:
                    return "others"
        except (OSError, UnidentifiedImageError):
            print(f"Skipped file {image_path}: Unidentified image format")
            return "others"

    def process_images(self):
        """
        處理源目錄中的所有圖片，根據分類結果進行移動
        """
        FileUtils.create_directory(self.target_path)
        count = 0

        for filename in os.listdir(self.source_path):
            sanitized_filename = self.sanitize_filename(filename)
            image_path = os.path.join(self.source_path, filename)

            if filename.endswith(".gif"):
                category = "gif"
            elif filename.endswith((".png", ".jpg", ".jpeg", ".jfif", ".JPG")):
                category = self.classify_wallpaper(image_path)
            else:
                print(f"Skipping file {filename}: Invalid image format")
                continue

            # 更新目標目錄
            category_path = os.path.join(self.target_path, category)
            FileUtils.create_directory(category_path)
            
            # 移動文件到分類後的目標目錄
            FileUtils.move_file(image_path, category_path, sanitized_filename)
            count += 1

        print(f"Processed {count} files.")

    def process_images(self):
        """
        遍歷圖片並根據條件分類為桌布
        """
        for filename in os.listdir(self.source_dir):
            file_path = os.path.join(self.source_dir, filename)
            if os.path.isfile(file_path) and filename.lower().endswith((".jpg", ".jpeg", ".png")):
                # 模擬判斷圖片是否符合條件（僅示例）
                if self.is_wallpaper(file_path):
                    move_file(file_path, self.target_dir, filename)
                    print(f"Classified {filename} as wallpaper.")

    def is_wallpaper(self, file_path):
        """
        判斷圖片是否符合桌布條件（僅示例）
        Returns:
            bool: 是否符合條件
        """
        # 此處可以根據圖片屬性進行判斷
        return True  # 暫時假設所有圖片符合條件
    
if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()

    source_path = os.getenv("SOURCE_DIRECTORY")
    target_path = os.getenv("TARGET_DIRECTORY")
    long_edge_threshold = int(os.getenv("LONG_EDGE_THRESHOLD"))
    short_edge_threshold = int(os.getenv("SHORT_EDGE_THRESHOLD"))
    aspect_ratio_threshold = float(os.getenv("ASPECT_RATIO_THRESHOLD"))

    classifier = WallpaperClassifier(source_path, target_path, long_edge_threshold, short_edge_threshold, aspect_ratio_threshold)
    classifier.process_images()
    
    