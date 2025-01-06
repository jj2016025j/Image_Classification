from ai_image.prompt.data.lighting_tone_filter_params import FILTER_PROMPTS, LIGHTING_PROMPTS, TONE_PROMPTS
from ai_image.utils import weighted_sample

class LightingPrompts:
    def __init__(self):
        # 光影提示詞與權重
        self.prompts = LIGHTING_PROMPTS
        
    def generate_prompts(self, count=1, mode='positive'):
        return weighted_sample(self.prompts, count, mode=mode)

class TonePrompts:
    def __init__(self):
        # 色調提示詞與權重
        self.prompts = TONE_PROMPTS

    def generate_prompts(self, count=1, mode='positive'):
        return weighted_sample(self.prompts, count, mode=mode)

class FilterPrompts:
    def __init__(self):
        # 濾鏡提示詞與權重
        self.prompts = FILTER_PROMPTS

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
