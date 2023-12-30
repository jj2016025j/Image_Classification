import os
import requests
from bs4 import BeautifulSoup
import re

def sanitize_filename(filename):
    # 移除不合法的字符
    s = re.sub(r'[\\/:*?"<>|]', '', filename)
    return s

def download_images_from_url(url, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Failed to retrieve the webpage.")
        return

    soup = BeautifulSoup(response.content, 'html.parser')

    # 尋找所有圖片標籤
    img_tags = soup.find_all('img')

    for img_tag in img_tags:
        img_url = img_tag.get('src')

        # 如果圖片 URL 不是完整的，則可能需要做額外處理（如拼接主域名等）
        # 這裡我們只處理完整的 URL
        if img_url.startswith("http"):
            img_name = os.path.basename(img_url)
            img_path = os.path.join(destination_folder, img_name)
            img_content = requests.get(img_url, headers=headers).content

            filename = sanitize_filename(webpage_url)
            img_path = os.path.join(destination, filename)
            with open(img_path, 'wb') as img_file:
                img_file.write(img_content)
            print(f"Downloaded {img_url} to {img_path}")

if __name__ == "__main__":
    webpage_url = "https://www.jkforum.net/thread-15842917-1-1.html"
    destination = "C:\\Users\\User\\Desktop\\test"
    
    download_images_from_url(webpage_url, destination)
