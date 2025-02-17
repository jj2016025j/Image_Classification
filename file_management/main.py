from file_management.core.cleaner import DirectoryCleaner
from file_management.core.wallpaper_classifier import wallpaper_classifier_main
from file_management.core.zip_operations import ZipOperations
from file_management.config.image_config import SOURCE_DIRECTORY

if __name__ == "__main__":
    print("\n開始桌布圖片分類...")
    wallpaper_classifier_main()

    print("\n解壓縮 ZIP 檔案...")
    ZipOperations.extract_zip_files(SOURCE_DIRECTORY)

    print("\n清理分類後的空資料夾...")
    DirectoryCleaner.clear_folder(SOURCE_DIRECTORY)

    print("\n所有作業已完成！")
