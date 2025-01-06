import random

from ai_image.prompt.data.environment_params import ATMOSPHERE_PARAMS, INDOOR_PARAMS, OUTDOOR_PARAMS, SEASON_PARAMS
from ai_image.utils import weighted_sample

class Background:
    def __init__(self):
        self.outdoor = OUTDOOR_PARAMS
        self.indoor = INDOOR_PARAMS
        
    def generate_background(self, count=1, mode='positive', theme='realistic'):
        """
        根據主題選擇室內或室外背景提示詞。
        :param count: 選擇的項目數量。
        :param theme: 主題類型（realistic / other future extensions）。
        :return: 隨機背景提示詞。
        """
        if theme == 'realistic':
            # 隨機選擇室內或室外，然後從中抽取提示詞
            choice = random.choice(['indoor', 'outdoor'])
            if choice == 'indoor':
                return weighted_sample(self.indoor, count, mode=mode)
            else:
                return weighted_sample(self.outdoor, count, mode=mode)
        else:
            raise ValueError("Unsupported theme")

class Season:
    def __init__(self):
        self.seasons = SEASON_PARAMS

    def generate_season(self, mode='positive'):
        return weighted_sample(self.seasons, count=1, mode=mode)

class Atmosphere:
    def __init__(self):
        self.atmosphere = ATMOSPHERE_PARAMS

    def generate_atmosphere(self, mode='positive'):
        return weighted_sample(self.atmosphere, count=1, mode=mode)

class EnvironmentGenerator:
    def __init__(self):
        self.background = Background()
        self.season = Season()
        self.atmosphere = Atmosphere()

    def generate_environment(self, theme='realistic'):
        background = self.background.generate_background(theme=theme)
        season = self.season.generate_season()
        atmosphere = self.atmosphere.generate_atmosphere()

        return background + season + atmosphere
        
# 測試程式
if __name__ == "__main__":
    generator = EnvironmentGenerator()
    environment = generator.generate_environment(theme='realistic')
    print("生成的環境提示詞:", environment)
