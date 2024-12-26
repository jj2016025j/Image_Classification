from PIL import Image
import imagehash

# is_similar.py
def is_similar(img1_path, img2_path):
    """
    比較兩張圖片的相似性
    :param img1_path: 第一張圖片的路徑
    :param img2_path: 第二張圖片的路徑
    :return: 布林值，表示是否相似
    """

    try:
        hash0 = imagehash.average_hash(Image.open(img1_path)) 
        hash1 = imagehash.average_hash(Image.open(img2_path)) 
        return hash0 == hash1
    except Exception as e:
        print(f"Error comparing images: {e}")
        return False