import os
from dotenv import load_dotenv
from classify_files import FileClassifier
from wallpaper_classifier import WallpaperClassifier

def main():
    """
    主函數，用於執行文件分類和圖片分類操作
    """
    # 加載環境變量
    load_dotenv()
    source_directory = os.getenv("SOURCE_DIRECTORY")
    target_directory = os.getenv("TARGET_DIRECTORY")
    long_edge_threshold = int(os.getenv("LONG_EDGE_THRESHOLD"))
    short_edge_threshold = int(os.getenv("SHORT_EDGE_THRESHOLD"))
    aspect_ratio_threshold = float(os.getenv("ASPECT_RATIO_THRESHOLD"))

    # 文件擴展名和目標目錄的映射
    extensions_mapping = {
        'images': ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.jfif', ".JPG"),
        'videos': ('.mp4', '.avi', '.mov', '.mkv', '.mp4v'),
        'audios': ('.mp3', '.wav', '.flac', '.aac'),
        'documents': ('.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.txt')
    }

    # 文件分類
    file_classifier = FileClassifier(source_directory, target_directory, extensions_mapping)
    file_classifier.classify_files()

    # 分類桌布圖片
    image_source_directory = os.path.join(target_directory, 'images')
    wallpaper_classifier = WallpaperClassifier(image_source_directory, image_source_directory, long_edge_threshold, short_edge_threshold, aspect_ratio_threshold)
    wallpaper_classifier.process_images()

if __name__ == "__main__":
    main()

# pip install python-dotenv

from process_images import process_images

if __name__ == "__main__":
    # 設定來源與目標資料夾
    source_path = "C:/Users/User/GitHub/ImageClassification/test"
    target_path = "C:/Users/User/GitHub/ImageClassification/test"

    # 開始處理圖片
    process_images(source_path, target_path)