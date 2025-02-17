import os
from generate.utils.file_utils import FileUtils

class TextGenerator:
    """文字檔案生成器"""

    def __init__(self, folder, content="Hello, world!"):
        self.folder = folder
        self.content = content

    def generate(self):
        """生成包含指定內容的文字檔"""
        FileUtils.create_directory(self.folder)
        filename = os.path.join(self.folder, f"{FileUtils.generate_random_string()}.txt")
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(self.content)
        print(f"📄 Generated text file: {filename}")
