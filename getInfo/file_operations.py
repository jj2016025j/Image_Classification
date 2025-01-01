import os
import shutil

from getInfo.image_operations import get_basic_image_details, load_image

def get_all_files_in_directory(directory_path):
    """
    獲取資料夾內所有檔案的路徑
    """
    all_files = []
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            all_files.append(file_path)
    return all_files

def save_json_to_file(json_data, file_path):
    """
    將JSON數據保存到文件
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(json_data)
        print(f"JSON data saved to(JSON數據已保存到) {file_path}")
    except Exception as e:
        print(f"Error saving JSON to file(保存JSON文件時出錯): {e}")
        
        
def filter_and_move_images(directory_path, matched_directory, unmatched_directory, keys):
    """
    篩選圖片並移動到不同的資料夾
    """
    all_files = get_all_files_in_directory(directory_path)
    for file_path in all_files:
        if file_path.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif')):
            img = load_image(file_path)
            if img:
                details = get_basic_image_details(img)
                if details and contains_any_key(details['info'], keys):
                    print(f"移動文件到 {matched_directory}: {file_path}")
                    shutil.move(file_path, os.path.join(matched_directory, os.path.basename(file_path)))
                else:
                    print(f"移動文件到 {unmatched_directory}: {file_path}")
                    shutil.move(file_path, os.path.join(unmatched_directory, os.path.basename(file_path)))
                    
def contains_any_key(info, keys):
    """
    檢查 info 中是否包含指定的鍵名稱
    """
    return any(key in info for key in keys)
