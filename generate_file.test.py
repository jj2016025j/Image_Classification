from generate.core.file_generator import generate_files, generate_random_images_within_range
from generate.utils.file_utils import create_directory

if __name__ == "__main__":
    OUTPUT_DIR = "test_output"
    total_files = 20
    total_images = 10

    # 確保目標資料夾存在
    create_directory(OUTPUT_DIR)

    # 生成隨機文件
    print("Starting file generation...")
    generate_files(OUTPUT_DIR, total_files)

    # 生成隨機尺寸的圖片
    print("\nStarting random image generation...")
    generate_random_images_within_range(
        folder=OUTPUT_DIR,
        total_times=total_images,
        min_size=(1000, 1000),
        max_size=(5000, 5000)
    )

    print("\nAll tasks completed.")
