# main.py
from image_processing.core.image_operations import load_image
from ui.tkinter_helpers import create_canvas, create_root_window, resize_image
import tkinter as tk
from PIL import ImageTk

def image_viewer_main():
    """
    主函数，用于运行图像查看器
    """
    # 图像路径
    image_path = r"test.png"
    image = load_image(image_path)  # 加载图像
    if image is None:
        print(f"无法加载图像: {image_path}")
        return

    # 创建主窗口
    root = create_root_window()
    canvas = create_canvas(root)

    # 在Canvas中显示图像
    global photo  # 声明photo为全局变量
    photo = ImageTk.PhotoImage(image)
    canvas_image = canvas.create_image(0, 0, image=photo, anchor=tk.NW)

    # 监听窗口大小变化事件
    canvas.bind("<Configure>", lambda event: resize_image(event, canvas, canvas_image, image))

    # 运行Tkinter主循环
    root.mainloop()

if __name__ == "__main__":
    image_viewer_main()