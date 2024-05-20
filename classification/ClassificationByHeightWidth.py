import os
import cv2
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def select_directory(title):
    """
    顯示目錄選擇對話框，返回選擇的目錄路徑
    Args:
        title (str): 對話框標題
    Returns:
        str: 選擇的目錄路徑，如果未選擇則返回空字符串
    """
    directory = filedialog.askdirectory(title=title)
    return directory

def confirm_action(message):
    """
    顯示確認對話框，詢問用戶是否確認執行操作
    Args:
        message (str): 對話框顯示的消息
    Returns:
        bool: 用戶是否確認執行操作
    """
    return messagebox.askyesno(title="確認執行", message=message)

def classify_image(image_path, output_dir):
    """
    根據圖片的高寬比分類圖片，並移動到相應的目標目錄
    Args:
        image_path (str): 圖片文件路徑
        output_dir (str): 輸出目標目錄
    """
    img = cv2.imread(image_path)
    height, width, _ = img.shape

    if height > width:
        category = "height_greater_than_width"
    elif height == width:
        category = "height_equals_width"
    else:
        category = "height_less_than_width"

    target_dir = os.path.join(output_dir, category)
    os.makedirs(target_dir, exist_ok=True)
    shutil.move(image_path, os.path.join(target_dir, os.path.basename(image_path)))
    print(f'Moved {os.path.basename(image_path)} to {target_dir}')

def classify_images(source_dir, output_dir):
    """
    遍歷源目錄中的所有圖片，根據高寬比進行分類並移動到相應的目標目錄
    Args:
        source_dir (str): 源目錄
        output_dir (str): 輸出目標目錄
    """
    for root, _, files in os.walk(source_dir):
        for file in files:
            if file.endswith((".jpg", ".png")):
                filepath = os.path.join(root, file)
                classify_image(filepath, output_dir)

    # 清空原始資料夾
    shutil.rmtree(source_dir)
    print(f'Removed source directory: {source_dir}')

def main():
    """
    主函數，用於執行圖片分類操作
    """
    root = tk.Tk()
    root.withdraw()  # 隱藏主窗口

    source_dir = select_directory("選擇資料夾")
    if not source_dir:
        return
    output_dir = select_directory("選擇輸出資料夾")
    if not output_dir:
        return
    confirm = confirm_action("執行此操作會清空原始資料夾，是否繼續？")
    if not confirm:
        return

    classify_images(source_dir, output_dir)
    messagebox.showinfo(title="完成", message="已完成操作")

if __name__ == "__main__":
    main()
