from PIL import Image

class ImageOperations:
    """ 圖片處理類別 """

    @staticmethod
    def get_basic_image_details(img):
        """ 獲取圖片基本資訊 """
        return {
            "format": img.format,
            "mode": img.mode,
            "size": img.size,
            "info": img.info
        }
