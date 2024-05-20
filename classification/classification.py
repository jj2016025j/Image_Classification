import os
import shutil

def create_directories(base_dir, subdirs):
    """
    創建目標子目錄
    Args:
        base_dir (str): 基本目錄
        subdirs (list): 子目錄列表
    """
    for subdir in subdirs:
        dir_path = os.path.join(base_dir, subdir)
        os.makedirs(dir_path, exist_ok=True)

def get_target_directory(file_extension, extensions_mapping):
    """
    根據文件擴展名獲取目標目錄
    Args:
        file_extension (str): 文件擴展名
        extensions_mapping (dict): 文件擴展名和目標目錄的映射
    Returns:
        str: 目標目錄名稱
    """
    for category, extensions in extensions_mapping.items():
        if file_extension in extensions:
            return category
    return "other"

def move_files(source_dir, extensions_mapping, base_target_dir):
    """
    移動文件到目標目錄
    Args:
        source_dir (str): 源目錄
        extensions_mapping (dict): 文件擴展名和目標目錄的映射
        base_target_dir (str): 基本目標目錄
    """
    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)
        
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1].lower()
            target_subdir = get_target_directory(file_extension, extensions_mapping)
            target_dir = os.path.join(base_target_dir, target_subdir)
            shutil.move(file_path, os.path.join(target_dir, filename))
            print(f'Moved {filename} to {target_dir}')

def classify_files(source_dir, base_target_dir):
    """
    主函數，用於分類文件並移動到相應目標目錄
    Args:
        source_dir (str): 源目錄
        base_target_dir (str): 基本目標目錄
    """
    subdirs = ['images', 'videos', 'audios', 'documents', 'other']
    create_directories(base_target_dir, subdirs)

    extensions_mapping = {
        'images': ('.jpg', '.jpeg', '.png', '.gif', '.bmp'),
        'videos': ('.mp4', '.avi', '.mov', '.mkv'),
        'audios': ('.mp3', '.wav', '.flac', '.aac'),
        'documents': ('.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.txt')
    }

    move_files(source_dir, extensions_mapping, base_target_dir)

if __name__ == "__main__":
    source_directory = "C:/Users/User/GitHub/ImageClassification/test"
    target_directory = "C:/Users/User/GitHub/ImageClassification/test"
    classify_files(source_directory, target_directory)
