import os
import shutil
from PIL import Image
# 定義一個函數來獲取圖片的副檔名
# 定義一個函數來獲取圖片的解析度
def get_resolution(image_path):
    with Image.open(image_path) as im:
        width, height = im.size
    return (width, height)

# 如果文件為圖像檔，則進行處理
def classify(image_path,extension):

    # 圖像處理代碼    
    if extension in [".jpg", ".jpeg", ".png"]:
        try:                
            # 獲取圖片的解析度 
            resolution = get_resolution(image_path)

            # 創建目標目錄的子目錄，以便按照解析度分類圖片
            if resolution[0] >= 7680 or resolution[1] >= 7680:
                target_subdir = "4320P (UHD 8K)"
            elif resolution[0] >= 3840 or resolution[1] >= 3840:
                target_subdir = "2160P (UHD 4K)"
            elif resolution[0] >= 1920 or resolution[1] >= 1920:
                target_subdir = "1080P (Full HD)"
            elif resolution[0] >= 960 or resolution[1] >= 960:
                target_subdir = "720P (HD)"
            else:
                target_subdir = "480P (SD)"

        # 圖像檔讀取失敗，略過該檔案
        except Exception:
            target_subdir = "other"

    # 如果文件為動態圖檔，則進行處理
    elif extension in [".gif"]:
            target_subdir = "gif"

    # 如果文件為影像檔，則進行處理
    elif extension in [".mp4"]:
            target_subdir = "mp4"

    else:
        # 創建目標目錄的新子目錄，以便放置非圖片檔
        target_subdir = "other"

    return target_subdir

# 定義一個函數來分類圖片
def classify_images(source_directory, target_directory):
    # 如果目標目錄不存在，則創建它
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)
    i=0
    j=0
    k=0
    l=0
    # 遍歷源目錄中的所有圖片和子目錄
    for root, dirs, files in os.walk(source_directory):
        for image_name in files:
            # 獲取圖片的完整路徑
            image_path = os.path.join(root, image_name)

            # 獲取文件的擴展名
            extension = os.path.splitext(image_path)[1]

            #分類圖片
            target_subdir = classify(image_path,extension)
            
            target_subdir_path = os.path.join(target_directory, target_subdir)
            if not os.path.exists(target_subdir_path):
                os.makedirs(target_subdir_path)
                
                
            #如果來源位置跟目標位置在同一個硬碟，則用os.rename進行處理    
            if os.stat(source_directory).st_dev == os.stat(target_directory).st_dev:
                
                # 如果檔案不存在，則建立檔案
                if not os.path.exists(os.path.join(target_subdir_path, image_name)):
                    # 將圖片移動到目標目錄的子目錄，如果文件不是圖像檔，則複製它到目標目錄的新子目錄
                    os.rename(image_path, os.path.join(target_subdir_path, image_name))
                    i=i+1
                    print(str(i)+"同硬碟移動"+"從"+str(image_path)+"到"+str(os.path.join(target_subdir_path, image_name)))
                    
                # 如果檔案存在，則取代檔案
                elif os.path.exists( os.path.join(target_subdir_path, image_name)):
                    # 先刪除目標目錄中的同名檔案
                    os.remove( os.path.join(target_subdir_path, image_name))
                    # 將圖片移動到目標目錄的子目錄，如果文件不是圖像檔，則複製它到目標目錄的新子目錄
                    os.rename(image_path, os.path.join(target_subdir_path, image_name))
                    j=j+1   
                    print("同硬碟移動"+str(i)+"從"+str(image_path)+"到"+str(os.path.join(target_subdir_path, image_name)))
            
            #如果來源位置跟目標位置在不同硬碟，則用shutil.copy進行處理                            
            else:
                # 如果檔案不存在，則建立檔案
                if not os.path.exists(os.path.join(target_subdir_path, image_name)):
                    shutil.copy(image_path, os.path.join(target_subdir_path, image_name))
                    # 刪除源文件
                    os.remove(image_path)
                    k=k+1
                    print("不同硬碟移動"+str(k)+"從"+str(image_path)+"到"+str(os.path.join(target_subdir_path, image_name))) 

                # 如果檔案存在，則取代檔案
                elif os.path.exists( os.path.join(target_subdir_path, image_name)):
                    # 先刪除目標目錄中的同名檔案
                    os.remove( os.path.join(target_subdir_path, image_name))
                    # 如果來源位置跟目標位置不在同一個硬碟，則將圖像複製到暫存目錄
                    shutil.copy(image_path, os.path.join(target_subdir_path, image_name))
                    # 刪除源文件
                    os.remove(image_path)
                    l=l+1
                    print("不同硬碟取代"+str(l)+"從"+str(image_path)+"到"+str(os.path.join(target_subdir_path, image_name)))

        # 刪除剩下的空子目錄
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            if not os.listdir(dir_path):
                os.rmdir(dir_path)            
        # 如果子目錄中沒有文件或子目錄，則刪除它
        #if not dirs and not files:
        #    os.rmdir(root)
    print("同硬碟移動"+str(i) )
    print("同硬碟取代"+str(j))
    print("不同硬碟移動"+str(k)) 
    print("不同硬碟取代"+str(l))              

                

# 使用示例
classify_images("D:\\測試", "D:\\分類")
