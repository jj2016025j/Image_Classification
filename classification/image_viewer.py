import cv2
import tkinter as tk
from PIL import Image, ImageTk

def load_image(image_path):
    """
    加载图像并转换为PIL格式
    Args:
        image_path (str): 图像路径
    Returns:
        PIL.Image: 转换后的PIL图像
    """
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return Image.fromarray(image)

def create_root_window(title="Image Viewer"):
    """
    创建Tkinter主窗口
    Args:
        title (str): 窗口标题
        width (int): 窗口宽度
        height (int): 窗口高度
    Returns:
        Tk: Tkinter主窗口实例
    """
    root = tk.Tk()
    root.title(title)
    return root

def create_canvas(root, width=600, height=600):
    """
    创建Canvas控件
    Args:
        root (Tk): Tkinter主窗口实例
        width (int): Canvas宽度
        height (int): Canvas高度
    Returns:
        Canvas: Tkinter Canvas控件实例
    """
    canvas = tk.Canvas(root, width=width, height=height)
    canvas.pack(side="left", fill="both", expand=True)
    return canvas

def resize_image(event, canvas, canvas_image, image):
    """
    自动调整图像大小并更新Canvas
    Args:
        event: Tkinter事件对象
        canvas: Tkinter Canvas控件
        canvas_image: Canvas上的图像对象
        image: PIL图像
    """
    global photo  # 声明photo为全局变量

    # 获取窗口大小
    width = canvas.winfo_width()
    height = canvas.winfo_height()

    # 计算缩放比例
    scale = min(width / image.width, height / image.height)

    # 缩放图像
    resized_image = image.resize((int(image.width * scale), int(image.height * scale)))

    # 更新Canvas上的图像
    photo = ImageTk.PhotoImage(resized_image)
    canvas.itemconfigure(canvas_image, image=photo)

def image_viewer_main():
    """
    主函数，用于运行图像查看器
    """
    # 图像路径
    image_path = r"src\images\4556.jpg"
    image = load_image(image_path) # 加载图像 
    root = create_root_window() # 创建主窗口
    canvas = create_canvas(root) # 创建Canvas控件

    photo = ImageTk.PhotoImage(image)
    canvas_image = canvas.create_image(0, 0, image=photo, anchor=tk.NW) # 显示图像

    canvas.bind("<Configure>", lambda event: resize_image(event, canvas, canvas_image, image))# 监听窗口大小变化事件
    root.mainloop()# 运行Tkinter主循环
