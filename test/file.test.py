# main.py

from file_operations.cleaner import DirectoryCleaner
from file_operations.file_operations import FileOperations
from file_operations.file_renaming import FileRenaming
from file_operations.zip_operations import ZipOperations


if __name__ == "__main__":
    source_dir = "./source"
    target_dir = "./target"

    # 使用功能範例
    FileOperations.create_directory(target_dir)
    FileRenaming.rename_files_in_directory(source_dir)
    ZipOperations.extract_zip_files(source_dir)
    DirectoryCleaner.clear_folder(target_dir)
    FileOperations.clean_empty_directories(source_dir)
