import random
from image_utils import generate_image, generate_random_images
from video_utils import generate_video
from audio_utils import generate_audio
from text_utils import generate_text_file

# 全局配置
FILE_GENERATORS = {
    "image": generate_image,
    "video": generate_video,
    "audio": generate_audio,
    "text": generate_text_file
}

def generate_random_file(folder, file_type):
    """根据文件类型生成一个随机文件。"""
    generator = FILE_GENERATORS.get(file_type)
    if not generator:
        raise ValueError(f"Unsupported file type: {file_type}")
    generator(folder)
    print(f"Generated {file_type} file in folder: {folder}")

def generate_files(folder, total_files):
    """生成多个随机类型的文件。"""
    file_types = list(FILE_GENERATORS.keys())
    for i in range(total_files):
        file_type = random.choice(file_types)
        generate_random_file(folder, file_type)
        print(f"[{i + 1}/{total_files}] File generation complete.")

def generate_random_images_within_range(folder, total_times, min_size, max_size):
    """生成多个随机尺寸的图片。"""
    for i in range(total_times):
        generate_random_images(folder, min_size=min_size, max_size=max_size)
        print(f"[{i + 1}/{total_times}] Random image generation complete.")

def main():
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
    main()