# 檔案重命名
import os
from collections import defaultdict

def rename_files_in_directory(directory):
    """
    在指定目錄中重命名所有檔案，使檔名包含其副檔名類型和一個獨特的編號。
    Args:
        directory (str): 欲進行檔案重命名的目錄路徑。
    """
    # 用於儲存每種副檔名的檔案數量
    extension_counts = defaultdict(int)

    # 遍歷目錄中的所有檔案
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            # 獲取檔案的副檔名
            file_extension = os.path.splitext(filename)[1].lower()

            # 更新副檔名的計數
            extension_counts[file_extension] += 1

            # 生成新的檔名，格式為 副檔名_編號.副檔名
            new_filename = f"{file_extension[1:]}_{extension_counts[file_extension]}{file_extension}"
            new_filepath = os.path.join(directory, new_filename)

            # 重命名檔案
            os.rename(filepath, new_filepath)
            print(f"已將 '{filename}' 重命名為 '{new_filename}'")

# 使用範例，請替換為您的目錄路徑
directory = "/path/to/your/directory"  # 這裡替換為您的目錄路徑
rename_files_in_directory(directory)
