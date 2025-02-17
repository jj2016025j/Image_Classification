from generate.core.audio_generator import AudioGenerator
from generate.core.image_generator import ImageGenerator
from generate.core.text_generator import TextGenerator
from generate.core.video_generator import VideoGenerator

class FileGenerator:
    """統一的文件生成管理器"""

    FILE_TYPES = {
        "audio": AudioGenerator,
        "image": ImageGenerator,
        "text": TextGenerator,
        "video": VideoGenerator
    }

    def __init__(self, folder):
        self.folder = folder

    def generate(self, file_type):
        """根據檔案類型生成檔案"""
        generator_class = self.FILE_TYPES.get(file_type)
        if not generator_class:
            print(f"❌ Unsupported file type: {file_type}")
            return

        generator = generator_class(self.folder)
        generator.generate()

    def generate_batch(self, file_types, count):
        """批次生成多個文件"""
        for _ in range(count):
            file_type = random.choice(file_types)
            self.generate(file_type)
