import random

def weighted_sample(option_dict, count=1):
    """
    根據權重隨機選擇不重複的項目。
    :param option_dict: 包含提示詞和權重的字典。
    :param count: 選擇的項目數量。
    :return: 不重複選擇的項目列表。
    """
    keys = list(option_dict.keys())
    weights = list(option_dict.values())
    selected_items = []
    while len(selected_items) < min(count, len(keys)):
        choice = random.choices(population=keys, weights=weights, k=1)[0]
        if choice not in selected_items:
            selected_items.append(choice)
    return selected_items

class Background:
    def __init__(self):
        self.outdoor = {
            'skyscrapers': 0.8,  # 高樓大廈
            'countryside cottage': 0.7,  # 鄉村小屋
            'forest': 0.9,  # 森林
            'desert': 0.6,  # 沙漠
            'beach': 0.8,  # 海邊
            'mountains': 0.9,  # 山脈
            'garden': 0.7,  # 花園
            'castle': 0.6,  # 城堡
            'waterfall': 0.8  # 瀑布
        }

        self.indoor = {
            'living room': 0.9,  # 客廳
            'kitchen': 0.8,  # 廚房
            'bedroom': 0.9,  # 臥室
            'office': 0.7,  # 辦公室
            'library': 0.8,  # 書房
            'bathroom': 0.6,  # 浴室
            'studio': 0.7,  # 工作室
            'hall': 0.6,  # 大廳
            'church': 0.5  # 教堂
        }

    def generate_background(self, count=1, theme='realistic'):
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
                return weighted_sample(self.indoor, count)
            else:
                return weighted_sample(self.outdoor, count)
        else:
            raise ValueError("Unsupported theme")

class Season:
    def __init__(self):
        self.seasons = {
            'spring': 0.8,  # 春
            'summer': 0.9,  # 夏
            'autumn': 0.7,  # 秋
            'winter': 0.9,  # 冬
            'rainy season': 0.5,  # 雨季
            'dry season': 0.4,  # 乾季
            'snow season': 0.6,  # 雪季
            'typhoon season': 0.3  # 颱風季
        }

    def generate_season(self):
        return weighted_sample(self.seasons, count=1)

class Atmosphere:
    def __init__(self):
        self.atmosphere = {
            'warm': 0.9,  # 溫暖
            'gloomy': 0.6,  # 陰森
            'romantic': 0.8,  # 浪漫
            'mysterious': 0.7,  # 神秘
            'relaxed': 0.9,  # 輕鬆
            'tense': 0.5,  # 緊張
            'fantastical': 0.6,  # 奇幻
            'futuristic': 0.4,  # 未來感
            'surreal': 0.5,  # 超現實
            'classical': 0.8  # 古典
        }

    def generate_atmosphere(self):
        return weighted_sample(self.atmosphere, count=1)

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
