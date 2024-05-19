# 下載某網站圖片 並且有設定闊值
import os
import requests
from bs4 import BeautifulSoup
from io import BytesIO
from PIL import Image
from urllib.parse import urljoin

# 設定解析度閾值
thresholds = {
    '720p': 921600,   # 1280x720
    '1080p': 2073600, # 1920x1080
    '2K': 2211840,    # 2048x1080
    '4K': 8294400,    # 3840x2160
    '8K': 33177600    # 7680x4320
}

# 設定圖片解析度的閾值
threshold = 10000


# 組成網頁的 URL
url = "https://www.jkforum.net/plugin/?id=voted&ac=view&vid=1421"

# 設定圖片存放目錄
destination_folder = "C:/Users/User/Github/ImageClassification/test"
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# 發出 HTTP GET 請求
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

response = requests.get(url, headers=headers)

if response.status_code != 200:
    print("Failed to retrieve the webpage.")
    exit()

# 使用 BeautifulSoup 解析 HTML
soup = BeautifulSoup(response.content, "html.parser")

# 取得網頁中所有圖片的網址
image_urls = []
for img in soup.find_all("img"):
    img_url = img.get("src")
    # 處理相對 URL
    img_url = urljoin(url, img_url)
    image_urls.append(img_url)
    print(img_url)

# 從圖片網址中下載圖片
for i, image_url in enumerate(image_urls):
    try:
        # 請求圖片的解析度資訊
        img_response = requests.get(image_url, headers={"Range": "bytes=0-9"})
        
        # 取得圖片的寬度和高度
        image = Image.open(BytesIO(img_response.content))
        width, height = image.size

        # 計算圖片的解析度
        resolution = width * height
        print(f"Image {i+1}: resolution = {resolution}, URL = {image_url}")

        # 判斷圖片的解析度是否大於等於閾值
        if resolution >= threshold:
            # 下載圖片
            img_response = requests.get(image_url)
            img_response.raise_for_status()  # 確保請求成功

            # 将圖片個別存檔，檔名為「image-1.jpg」、「image-2.jpg」、「image-3.jpg」……
            image_data = img_response.content
            img_name = f"image-{i+1}.jpg"
            img_path = os.path.join(destination_folder, img_name)

            with open(img_path, "wb") as f:
                f.write(image_data)
                print(f"Downloaded {image_url} to {img_path}")

        else:
            # 圖片的解析度不符合要求，跳過下載
            print(f"Image {i+1}: resolution does not meet the threshold, skipping download.")

    except Exception as e:
        print(f"Error processing image {image_url}: {e}")
