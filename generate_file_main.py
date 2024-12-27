
from generate.generated_file import generate_files, generate_random_images_within_range

def generate_file_func():
    from ai_image.config import OUTPUT_DIR
    total_files = 20
    total_images = 10

    # 生成随机文件
    print("Starting file generation...")
    generate_files(OUTPUT_DIR, total_files)

    # 生成随机尺寸的图片
    print("\nStarting random image generation...")
    generate_random_images_within_range(
        folder=OUTPUT_DIR,
        total_times=total_images,
        min_size=(1000, 1000),
        max_size=(5000, 5000)
    )
    print("\nAll tasks completed.")

if __name__ == "__main__":
    generate_file_func()