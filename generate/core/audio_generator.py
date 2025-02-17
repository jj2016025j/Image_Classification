import os
from pydub.generators import Sine
from generate.utils.file_utils import FileUtils
from generate.config import AUDIO_FREQUENCY, AUDIO_DURATION

class AudioGenerator:
    """音訊檔案生成器"""

    def __init__(self, folder):
        self.folder = folder

    def generate(self):
        """生成正弦波音頻"""
        FileUtils.create_directory(self.folder)
        filename = os.path.join(self.folder, f"{FileUtils.generate_random_string()}.wav")
        tone = Sine(AUDIO_FREQUENCY).to_audio_segment(duration=AUDIO_DURATION)
        tone.export(filename, format='wav')
        print(f"🎵 Generated audio: {filename}")
