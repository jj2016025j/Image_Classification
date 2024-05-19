import os
import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin

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

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to retrieve the webpage: {e}")
        return

    soup = BeautifulSoup(response.content, 'html.parser')

    # 尋找所有圖片標籤
    img_tags = soup.find_all('img')

    for img_tag in img_tags:
        img_url = img_tag.get('src')

        # 處理相對 URL
        img_url = urljoin(url, img_url)

        if img_url.startswith("http"):
            img_name = sanitize_filename(os.path.basename(img_url))
            img_path = os.path.join(destination_folder, img_name)
            
            try:
                img_content = requests.get(img_url, headers=headers).content
                with open(img_path, 'wb') as img_file:
                    img_file.write(img_content)
                print(f"Downloaded {img_url} to {img_path}")
            except requests.RequestException as e:
                print(f"Failed to download {img_url}: {e}")
            except OSError as e:
                print(f"Failed to save {img_url} to {img_path}: {e}")

if __name__ == "__main__":
    webpage_url = "https://www.jkforum.net/thread-15842917-1-1.html"
    destination = "C:/Users/User/Github/ImageClassification/test"
    
    download_images_from_url(webpage_url, destination)
