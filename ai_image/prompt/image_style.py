import random

class ImageStyle:
    def __init__(self):
        # 風格類型及提示詞配置
        self.styles = {
            'realistic': {
                'prompts': {
                    'photo realistic': {'positive': 1, 'negative': 0.1},
                    'CG': {'positive': 0.8, 'negative': 0.2},
                    '3D rendering style': {'positive': 0.7, 'negative': 0.3},
                    'artbook': {'positive': 0.6, 'negative': 0.4}
                }
            },
            'artistic': {
                'prompts': {
                    'hand-drawn style': {'positive': 1, 'negative': 0.1},
                    'illustration': {'positive': 0.9, 'negative': 0.2},
                    'fantasy': {'positive': 0.8, 'negative': 0.3},
                    'art nouveau': {'positive': 0.7, 'negative': 0.4},
                    'watercolor style': {'positive': 0.6, 'negative': 0.5},
                    'oil painting style': {'positive': 0.7, 'negative': 0.4},
                    'sketch style': {'positive': 0.5, 'negative': 0.6}
                }
            },
            'anime': {
                'prompts': {
                    'anime': {'positive': 1, 'negative': 0.1},
                    'anime coloring': {'positive': 0.9, 'negative': 0.2},
                    '2D': {'positive': 0.8, 'negative': 0.3},
                    'comic style': {'positive': 0.7, 'negative': 0.4},
                    'pixel art': {'positive': 0.6, 'negative': 0.5}
                }
            },
            'historical': {
                'prompts': {
                    'impressionism': {'positive': 1, 'negative': 0.1},
                    'baroque': {'positive': 0.8, 'negative': 0.3},
                    'retro style': {'positive': 0.7, 'negative': 0.4}
                }
            }
        }

    def get_prompts(self, style_type, count=20, mode='positive'):
        """
        根據指定風格類型生成相關提示詞。
        :param style_type: 風格類型（如 'realistic', 'artistic' 等）。
        :param count: 返回提示詞的數量。
        :param mode: 選擇模式，可為 'positive' 或 'negative'。
        :return: 隨機選擇的提示詞列表。
        """
        if style_type not in self.styles:
            raise ValueError(f"Style type '{style_type}' does not exist. Available types: {list(self.styles.keys())}")

        # 提取風格類型的提示詞及對應權重
        prompts_with_weights = self.styles[style_type]['prompts']

        # 構建候選池
        candidates = [(prompt, weights[mode]) for prompt, weights in prompts_with_weights.items()]

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

    def get_image_style(self, mode='positive'):
        realistic = self.get_prompts('realistic', mode=mode)  # 獲取寫實風格
        artistic = self.get_prompts('artistic', mode=mode)    # 獲取藝術風格
        anime = self.get_prompts('anime', mode=mode)          # 獲取動畫風格
        historical = self.get_prompts('historical', mode=mode)  # 獲取歷史風格
        
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
