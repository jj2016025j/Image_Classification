import random

from ai_image.utils import weighted_sample

class Background:
    def __init__(self):
        self.outdoor = {
            'skyscrapers': {'positive': 0.8, 'negative': 0.2},
            'countryside cottage': {'positive': 0.7, 'negative': 0.3},
            'forest': {'positive': 0.9, 'negative': 0.1},
            'desert': {'positive': 0.6, 'negative': 0.4},
            'beach': {'positive': 0.8, 'negative': 0.2},
            'mountains': {'positive': 0.9, 'negative': 0.1},
            'garden': {'positive': 0.7, 'negative': 0.3},
            'castle': {'positive': 0.6, 'negative': 0.4},
            'waterfall': {'positive': 0.8, 'negative': 0.2}
        }

        self.indoor = {
            'living room': {'positive': 0.9, 'negative': 0.1},
            'kitchen': {'positive': 0.8, 'negative': 0.2},
            'bedroom': {'positive': 0.9, 'negative': 0.1},
            'office': {'positive': 0.7, 'negative': 0.3},
            'library': {'positive': 0.8, 'negative': 0.2},
            'bathroom': {'positive': 0.6, 'negative': 0.4},
            'studio': {'positive': 0.7, 'negative': 0.3},
            'hall': {'positive': 0.6, 'negative': 0.4},
            'church': {'positive': 0.5, 'negative': 0.5}
        }
        
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
        self.seasons = {
            'spring': {'positive': 0.8, 'negative': 0.2},
            'summer': {'positive': 0.9, 'negative': 0.1},
            'autumn': {'positive': 0.7, 'negative': 0.3},
            'winter': {'positive': 0.9, 'negative': 0.1},
            'rainy season': {'positive': 0.5, 'negative': 0.5},
            'dry season': {'positive': 0.4, 'negative': 0.6},
            'snow season': {'positive': 0.6, 'negative': 0.4},
            'typhoon season': {'positive': 0.3, 'negative': 0.7}
        }

    def generate_season(self, mode='positive'):
        return weighted_sample(self.seasons, count=1, mode=mode)

class Atmosphere:
    def __init__(self):
        self.atmosphere = {
            'warm': {'positive': 0.9, 'negative': 0.1},
            'gloomy': {'positive': 0.6, 'negative': 0.4},
            'romantic': {'positive': 0.8, 'negative': 0.2},
            'mysterious': {'positive': 0.7, 'negative': 0.3},
            'relaxed': {'positive': 0.9, 'negative': 0.1},
            'tense': {'positive': 0.5, 'negative': 0.5},
            'fantastical': {'positive': 0.6, 'negative': 0.4},
            'futuristic': {'positive': 0.4, 'negative': 0.6},
            'surreal': {'positive': 0.5, 'negative': 0.5},
            'classical': {'positive': 0.8, 'negative': 0.2}
        }

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
