import os
import random
import string
from PIL import Image
import cv2
import numpy as np
from pydub import AudioSegment
from pydub.generators import Sine

def generate_random_string(length):
    characters = string.ascii_letters + string.digits + '_'
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

def generate_image(folder, size=(100, 100), color=(255, 0, 0)):
    filename = os.path.join(folder, generate_random_string(12) + '.png')
    image = Image.new('RGB', size, color)
    image.save(filename)
    print(f"Generated image: {filename}")

def generate_random_images(folder, min_size=(50, 50), max_size=(500, 500), color=(255, 0, 0)):
    """
    生成隨機大小的圖片並保存到指定目錄
    Args:
        folder (str): 保存圖片的目錄
        min_size (tuple): 圖片的最小尺寸 (width, height)
        max_size (tuple): 圖片的最大尺寸 (width, height)
        color (tuple): 圖片的顏色 (R, G, B)
    """
    if not os.path.exists(folder):
        os.makedirs(folder)
        
    width = random.randint(min_size[0], max_size[0])
    height = random.randint(min_size[1], max_size[1])
    filename = os.path.join(folder, generate_random_string(12) + '.png')
    image = Image.new('RGB', (width, height), color)
    image.save(filename)
    print(f"Generated image: {filename}, Size: {width}x{height}")

def generate_video(folder, width=640, height=480, fps=30, duration=5):
    filename = os.path.join(folder, generate_random_string(12) + '.avi')
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(filename, fourcc, fps, (width, height))
    
    for _ in range(int(fps * duration)):
        frame = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
        out.write(frame)
    
    out.release()
    print(f"Generated video: {filename}")

def generate_audio(folder, duration=1000, frequency=440):
    filename = os.path.join(folder, generate_random_string(12) + '.wav')
    tone = Sine(frequency).to_audio_segment(duration=duration)
    tone.export(filename, format='wav')
    print(f"Generated audio: {filename}")

def generate_text_file(folder, content):
    filename = os.path.join(folder, generate_random_string(12) + '.txt')
    with open(filename, 'w') as file:
        file.write(content)
    print(f"Generated text file: {filename}")

def generate_files(test_folder, total_files):
    if not os.path.exists(test_folder):
        os.makedirs(test_folder)

    file_types = ['image', 'video', 'audio', 'text']

    for _ in range(total_files):
        file_type = random.choice(file_types)
        if file_type == 'image':
            generate_image(test_folder)
        elif file_type == 'video':
            generate_video(test_folder)
        elif file_type == 'audio':
            generate_audio(test_folder)
        elif file_type == 'text':
            generate_text_file(test_folder, 'Hello, world!\nThis is an example text file.')
        print(f'NO.{_}')

    print(f"Generated {total_files} files in {test_folder}")

def repeatFunction(total_time, func_name, test_folder, *args, **kwargs):
    for _ in range(total_time):
        func_name(test_folder, *args, **kwargs)

if __name__ == "__main__":
    # 設定目標資料夾和要生成的文件總數量
    test_folder = './test/'
    total_files = 20

    # 調用生成文件的函數
    # generate_files(test_folder, total_files)
    
    # 生成指定數量隨機畫質的內容
    repeatFunction(
        total_files,
        generate_random_images,
        test_folder, 
        min_size=(50, 50),
        max_size=(5000, 5000)
        
    )