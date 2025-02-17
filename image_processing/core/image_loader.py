from PIL import Image, UnidentifiedImageError
import cv2

class ImageLoader:
    """ 圖片載入類別 """

    @staticmethod
    def load_image(image_path, use_opencv=False, show=False):
        """ 載入圖片 """
        try:
            if use_opencv:
                image = cv2.imread(image_path)
                if image is None:
                    raise FileNotFoundError(f"Image not found: {image_path}")
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                image = Image.fromarray(image)
            else:
                image = Image.open(image_path)
                image.load()  # 確保圖像完全加載
            if show:
                image.show()
            return image
        except Exception as e:
            print(f"無法載入圖片: {e}")
            return None
