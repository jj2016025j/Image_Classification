from ai_image.utils import weighted_sample

class LightingPrompts:
    def __init__(self):
        # 光影提示詞與權重
        self.prompts = {
            'Bright': {'positive': 1, 'negative': 0.1},
            'Soft': {'positive': 0.8, 'negative': 0.2},
            'Backlight': {'positive': 0.7, 'negative': 0.3},
            'backlit': {'positive': 0.7, 'negative': 0.3},
            'side-lit': {'positive': 0.7, 'negative': 0.3},
            'moonlight': {'positive': 0.7, 'negative': 0.3},
            'candlelight': {'positive': 0.7, 'negative': 0.3},
            'starlight': {'positive': 0.7, 'negative': 0.3},
            'sunlight': {'positive': 0.7, 'negative': 0.3},
            'dusk light': {'positive': 0.7, 'negative': 0.3},
            'morning light': {'positive': 0.7, 'negative': 0.3},
            'lightning': {'positive': 0.7, 'negative': 0.3},
        }
        
    def generate_prompts(self, count=1, mode='positive'):
        return weighted_sample(self.prompts, count, mode=mode)

class TonePrompts:
    def __init__(self):
        # 色調提示詞與權重
        self.prompts = {
            'Cool': {'positive': 1, 'negative': 0.1},
            'Warm': {'positive': 0.8, 'negative': 0.2},
            'Monochrome': {'positive': 0.7, 'negative': 0.3},
        }

    def generate_prompts(self, count=1, mode='positive'):
        return weighted_sample(self.prompts, count, mode=mode)

class FilterPrompts:
    def __init__(self):
        # 濾鏡提示詞與權重
        self.prompts = {
            'Vintage': {'positive': 1, 'negative': 0.1},
            'HDR': {'positive': 0.9, 'negative': 0.2},
            'Black and White': {'positive': 0.8, 'negative': 0.3},
        }

    def generate_prompts(self, count=1, mode='positive'):
        return weighted_sample(self.prompts, count, mode=mode)

# 測試程式
if __name__ == "__main__":
    # 建立各個類別的實例
    lighting = LightingPrompts()
    tone = TonePrompts()
    filter_prompts = FilterPrompts()

    # 生成提示詞
    lighting_prompt = lighting.generate_prompts(count=1, mode='positive')
    tone_prompt = tone.generate_prompts(count=1, mode='positive')
    filter_prompt = filter_prompts.generate_prompts(count=1, mode='positive')

    print("光影提示詞:", lighting_prompt)
    print("色調提示詞:", tone_prompt)
    print("濾鏡提示詞:", filter_prompt)
