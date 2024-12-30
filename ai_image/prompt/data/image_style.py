import random

class ImageStyle:
    def __init__(self):
        # 風格類型及提示詞配置
        self.styles = {
            'realistic': {
                'prompts': {
                    'photo realistic': 1,
                    'CG': 0.8,
                    '3D rendering style': 0.7,
                    'artbook': 0.6
                }
            },
            'artistic': {
                'prompts': {
                    'hand-drawn style': 1,
                    'illustration': 0.9,
                    'fantasy': 0.8,
                    'art nouveau': 0.7,
                    'watercolor style': 0.6,
                    'oil painting style': 0.7,
                    'sketch style': 0.5
                }
            },
            'anime': {
                'prompts': {
                    'anime': 1,
                    'anime coloring': 0.9,
                    '2D': 0.8,
                    'comic style': 0.7,
                    'pixel art': 0.6
                }
            },
            'historical': {
                'prompts': {
                    'impressionism': 1,
                    'baroque': 0.8,
                    'retro style': 0.7
                }
            }
        }

    def get_prompts(self, style_type, count=20):
        """
        根據指定風格類型生成相關提示詞。
        :param style_type: 風格類型（如 'realistic', 'artistic' 等）
        :param count: 返回提示詞的數量
        :return: 隨機選擇的提示詞列表
        """
        if style_type not in self.styles:
            raise ValueError(f"Style type '{style_type}' does not exist. Available types: {list(self.styles.keys())}")

        # 提取風格類型的提示詞及權重
        prompts_with_weights = self.styles[style_type]['prompts']

        # 構建候選池
        candidates = list(prompts_with_weights.items())

        # 必選提示詞（權重為 1）
        mandatory = [prompt for prompt, weight in candidates if weight == 1]

        # 可選提示詞（權重介於 0 和 1）
        optional = [(prompt, weight) for prompt, weight in candidates if 0 < weight < 1]

        # 從可選提示詞中按權重隨機選擇，且不重複
        optional_choices = []
        if optional:
            while len(optional_choices) < max(0, count - len(mandatory)) and optional:
                optional_prompts, optional_weights = zip(*optional)
                selected = random.choices(
                    population=optional_prompts,
                    weights=optional_weights,
                    k=1
                )[0]
                optional_choices.append(selected)
                optional = [(prompt, weight) for prompt, weight in optional if prompt != selected]

        # 合併必選和可選提示詞，並去重
        selected = list(set(mandatory + optional_choices))

        # 如果不足，從剩餘選項中補足
        remaining_candidates = [prompt for prompt, _ in candidates if prompt not in selected]
        if len(selected) < count:
            selected += random.sample(remaining_candidates, min(count - len(selected), len(remaining_candidates)))

        return selected[:count]

    def get_image_style(self):
        realistic = self.get_prompts('realistic')  # 獲取寫實風格
        artistic = self.get_prompts('artistic')    # 獲取藝術風格
        anime = self.get_prompts('anime')          # 獲取動畫風格
        historical = self.get_prompts('historical')  # 獲取歷史風格
        
        return realistic + artistic + anime + historical
        
# 測試
if __name__ == "__main__":
    style = ImageStyle()

    print("Realistic Style Prompts:")
    print(style.get_prompts('realistic'))

    print("Artistic Style Prompts:")
    print(style.get_prompts('artistic'))

    print("Anime Style Prompts:")
    print(style.get_prompts('anime'))

    print("Historical Style Prompts:")
    print(style.get_prompts('historical'))
    
    print(style.get_image_style())
