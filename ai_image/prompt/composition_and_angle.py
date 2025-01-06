from ai_image.prompt.data.prompts_params import COMPOSITION_PROMPTS, EFFECTS_PROMPTS, PERSPECTIVE_PROMPTS
from ai_image.utils import weighted_sample


class PerspectivePrompts:
    def __init__(self):
        # 視角提示詞與權重
        self.prompts = PERSPECTIVE_PROMPTS

    def generate_prompts(self, count=1, mode='positive'):
        return weighted_sample(self.prompts, count, mode=mode)
      
class CompositionPrompts:
    def __init__(self):
        # 構圖提示詞與權重
        self.prompts = COMPOSITION_PROMPTS

    def generate_prompts(self, count=1, mode='positive'):
        return weighted_sample(self.prompts, count, mode=mode)
      
class EffectsPrompts:
    def __init__(self):
        # 效果提示詞與權重
        self.prompts = EFFECTS_PROMPTS

    def generate_prompts(self, count=3, mode='positive'):
        return weighted_sample(self.prompts, count, mode=mode)
      
            
# 測試程式
if __name__ == "__main__":
    perspective = PerspectivePrompts()
    perspective_prompt = perspective.generate_prompts(count=1, mode='positive')
    print("視角提示詞:", perspective_prompt)
    
    composition = CompositionPrompts()
    composition_prompt = composition.generate_prompts(count=1, mode='positive')
    print("構圖提示詞:", composition_prompt)

    effects = EffectsPrompts()
    effects_prompt = effects.generate_prompts(count=3, mode='positive')
    print("效果提示詞:", effects_prompt)
