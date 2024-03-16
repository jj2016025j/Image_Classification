#解壓縮跟去除資料夾
import os
import shutil
import zipfile

def extract_files(src_dir):
    # 第一步：解压缩
    for root, files in os.walk(src_dir):
        for name in files:
            if name.endswith('.zip'):
                zip_path = os.path.join(root, name)
                with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                    zip_ref.extractall(root)
                os.remove(zip_path)
                
def move_files(src_dir, dst_dir):
    # 第二步和第三步：移动文件并删除原始文件夹
    for root, dirs, files in os.walk(src_dir, topdown=False):
        for name in files:
            src_file = os.path.join(root, name)
            dst_file = os.path.join(dst_dir, name)
            shutil.move(src_file, dst_file)
        
        for name in dirs:
            os.rmdir(os.path.join(root, name))

# 使用示例
source_directory = "C:\\Users\\User\\Desktop\\tablecloth\\classification - 複製"  # 替换为你的源路径
destination_directory = '/path/to/destination'  # 替换为你的目标路径

extract_files(source_directory)
move_files(source_directory, destination_directory)