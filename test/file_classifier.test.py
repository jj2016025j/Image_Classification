import os
from dotenv import load_dotenv

from file_operations.file_classifier import FileClassifier

def main():
    """
    主函數，用於執行文件分類操作
    """
    # 加載環境變量
    load_dotenv()
    source_directory = os.getenv("SOURCE_DIRECTORY")
    target_directory = os.getenv("TARGET_DIRECTORY")

    # 文件擴展名和目標目錄的映射
    extensions_mapping = {
        'images': ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.jfif', ".JPG"),
        'videos': ('.mp4', '.avi', '.mov', '.mkv', '.mp4v'),
        'audios': ('.mp3', '.wav', '.flac', '.aac'),
        'documents': ('.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.txt')
    }

    # 文件分類
    FileClassifier(source_directory, target_directory, extensions_mapping).classify_files()

if __name__ == "__main__":
    main()
