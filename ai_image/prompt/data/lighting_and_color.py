from ai_image.utils import weighted_sample

class LightingPrompts:
    def __init__(self):
        # 光影提示詞與權重
        self.prompts = {
            'Bright': 1,  # 明亮光影
            'Soft': 0.8,  # 柔和光影
            'Backlight': 0.7,  # 逆光效果
            'backlit': 0.7,  # 背光
            'side-lit': 0.7,  # 側光
            'moonlight': 0.7,  # 月光
            'candlelight': 0.7,  # 燭光
            'starlight': 0.7,  # 星光
            'sunlight': 0.7,  # 陽光
            'dusk light': 0.7,  # 黃昏光
            'morning light': 0.7,  # 晨光
            'lightning': 0.7,  # 閃電光
        }

    def generate_prompt(self, count=1):
        return weighted_sample(self.prompts, count)

class TonePrompts:
    def __init__(self):
        # 色調提示詞與權重
        self.prompts = {
            'Cool': 1,  # 冷色調
            'Warm': 0.8,  # 暖色調
            'Monochrome': 0.7  # 單色調
        }

    def generate_prompt(self, count=1):
        return weighted_sample(self.prompts, count)

class FilterPrompts:
    def __init__(self):
        # 濾鏡提示詞與權重
        self.prompts = {
            'Vintage': 1,  # 復古濾鏡
            'HDR': 0.9,  # 高動態範圍濾鏡
            'Black and White': 0.8  # 黑白濾鏡
        }

    def generate_prompt(self, count=1):
        return weighted_sample(self.prompts, count)

# 測試程式
if __name__ == "__main__":
    # 建立各個類別的實例
    lighting = LightingPrompts()
    tone = TonePrompts()
    filter_prompts = FilterPrompts()

    # 生成提示詞
    lighting_prompt = lighting.generate_prompt(count=1)
    tone_prompt = tone.generate_prompt(count=1)
    filter_prompt = filter_prompts.generate_prompt(count=1)

    print("光影提示詞:", lighting_prompt)
    print("色調提示詞:", tone_prompt)
    print("濾鏡提示詞:", filter_prompt)
