from PIL import Image
import imagehash

class ImageSimilarity:
    """ 圖片相似度判斷類別 """

    @staticmethod
    def is_similar(img1_path, img2_path):
        """ 比較兩張圖片是否相似 """
        try:
            hash0 = imagehash.average_hash(Image.open(img1_path)) 
            hash1 = imagehash.average_hash(Image.open(img2_path)) 
            return hash0 == hash1
        except Exception as e:
            print(f"Error comparing images: {e}")
            return False
