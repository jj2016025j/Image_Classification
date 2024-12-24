from PIL import ImageTk
import tkinter as tk
from file_operations.image_viewer import create_canvas, create_root_window, load_image, resize_image

def main():
    """
    主函数，用于运行图像查看器
    """
    # 图像路径
    image_path = "example.png"

    # 加载图像
    image = load_image(image_path)

    # 创建主窗口
    root = create_root_window()

    # 创建Canvas控件
    canvas = create_canvas(root, 800, 600)

    # 显示图像
    photo = ImageTk.PhotoImage(image)
    canvas_image = canvas.create_image(0, 0, image=photo, anchor=tk.NW)

    # 监听窗口大小变化事件
    canvas.bind("<Configure>", lambda event: resize_image(event, canvas, canvas_image, image))

    # 运行Tkinter主循环
    root.mainloop()

if __name__ == "__main__":
    main()
