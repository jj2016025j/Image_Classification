# 爬蟲
import requests
from bs4 import BeautifulSoup

# 定義函式，用來判斷圖片的解析度是否符合要求
def is_valid_image(img):
    # 這裡是判斷圖片解析度的程式碼
    # 假設圖片解析度符合要求，則回傳 True
    return True

# 要抓取的網站 URL
url = "https://www.youtube.com/watch?v=B5JX-vf048k"

# 向網站發出 HTTP GET 請求
response = requests.get(url)

# 取得網站的回應內容（網頁 HTML 文字）
html = response.text

# 使用 BeautifulSoup 解析 HTML
soup = BeautifulSoup(html, "lxml")

# 找出所有的圖片標籤
image_tags = soup.find_all("img")

# 逐一處理每個圖片標籤
for i, image_tag in enumerate(image_tags):
    # 取得圖片的 URL
    image_url = image_tag.get("src")
    
    # 向圖片的 URL 發出 HTTP GET 請求
    response = requests.get(image_url)
    
    # 如果圖片的解析度符合要求
    if is_valid_image(response):
        # 將圖片個別存檔，檔名為「image-1.jpg」、「image-2.jpg」、「image-3.jpg」……
        image_data = response.content
        with open(f"image-{i+1}.jpg", "wb") as f:
            f.write(image_data)
    else:
        # 圖片的解析度不符合要求，跳過下載
        pass
    
    
import requests
from io import BytesIO
from bs4 import BeautifulSoup
from PIL import Image

# 設定圖片解析度的閾值
threshold = 1000000

# 組成網頁的 URL
url = "https://www.youtube.com/watch?v=B5JX-vf048k"

# 下載網頁內容
response = requests.get(url)
html = response.text
###print(html)

# 使用 BeautifulSoup 解析網頁內容
soup = BeautifulSoup(html, "html.parser")

# 取得網頁中所有圖片的網址
image_urls = []
for img in soup.find_all("img"):
    image_url = img.get("src")
    image_urls.append(image_url)
    print(image_url)


# 從圖片網址中下載圖片
for i, image_url in enumerate(image_urls):
    # 請求圖片的解析度資訊
    response = requests.get(image_url, headers={"Range": "bytes=0-9"})

    # 取得圖片的寬度和高度
    image = Image.open(BytesIO(response.content))
    width, height = image.size

    # 計算圖片的解析度
    resolution = width * height
    ###print(resolution)

    # 判斷圖片的解析度是否大於等於閾值
    if resolution >= threshold:
        # 下載圖片
        response = requests.get(image_url)
        
    # 将圖片個別存檔，檔名為「image-1.jpg」、「image-2.jpg」、「image-3.jpg」……
        image_data = response.content
        with open("C:\\images\\image.jpg", "wb") as f:
            f.write(image_data)
            ###print(f)

    else:
        # 圖片的解析度不符合要求，跳過下載
        print("圖片的解析度不符合要求，跳過下載")

        pass
