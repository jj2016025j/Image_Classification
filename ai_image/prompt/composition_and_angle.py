from ai_image.utils import weighted_sample


class PerspectivePrompts:
    def __init__(self):
        # 視角提示詞與權重
        self.prompts = {
            'bird\'s eye view': {'positive': 0.9, 'negative': 0.1},
            'scorpion view': {'positive': 0.5, 'negative': 0.5},
            'top-down view': {'positive': 0.9, 'negative': 0.1},
            'low angle': {'positive': 0.8, 'negative': 0.2},
            'side angle': {'positive': 0.8, 'negative': 0.2},
            'front view': {'positive': 0.9, 'negative': 0.1},
            'close-up': {'positive': 0.9, 'negative': 0.1},
            'face-close-up': {'positive': 0.9, 'negative': 0.1},
            'long shot': {'positive': 0.7, 'negative': 0.3},
            'zoom out': {'positive': 0.6, 'negative': 0.4},
            'close up portrait': {'positive': 0.9, 'negative': 0.1},
            'dutch angle': {'positive': 0.7, 'negative': 0.3},
            'focused view': {'positive': 0.8, 'negative': 0.2}
        }

    def generate_prompts(self, count=1, mode='positive'):
        return weighted_sample(self.prompts, count, mode=mode)
      
class CompositionPrompts:
    def __init__(self):
        # 構圖提示詞與權重
        self.prompts = {
            'central composition': {'positive': 0.9, 'negative': 0.1},
            'diagonal composition': {'positive': 0.8, 'negative': 0.2},
            'golden ratio': {'positive': 0.9, 'negative': 0.1},
            'rule of thirds': {'positive': 0.9, 'negative': 0.1},
            'symmetrical composition': {'positive': 0.7, 'negative': 0.3},
            'asymmetrical composition': {'positive': 0.7, 'negative': 0.3},
            'framed composition': {'positive': 0.6, 'negative': 0.4},
            'leading lines': {'positive': 0.8, 'negative': 0.2},
            'minimal composition': {'positive': 0.5, 'negative': 0.5},
            'Half-body': {'positive': 0.4, 'negative': 0.6},
            'Full-body': {'positive': 0.5, 'negative': 0.5},
            'complex composition': {'positive': 0.4, 'negative': 0.6}
        }

    def generate_prompts(self, count=1, mode='positive'):
        return weighted_sample(self.prompts, count, mode=mode)
      
class EffectsPrompts:
    def __init__(self):
        # 效果提示詞與權重
        self.prompts = {
            'blur': {'positive': 0.6, 'negative': 0.4},
            'texture': {'positive': 0.8, 'negative': 0.2},
            'highlights': {'positive': 0.9, 'negative': 0.1},
            'shadows': {'positive': 0.9, 'negative': 0.1},
            'filter': {'positive': 0.7, 'negative': 0.3},
            'vintage effect': {'positive': 0.6, 'negative': 0.4},
            'glow': {'positive': 0.8, 'negative': 0.2},
            'gradient effect': {'positive': 0.5, 'negative': 0.5},
            'distortion': {'positive': 0.4, 'negative': 0.6},
            'refraction effect': {'positive': 0.6, 'negative': 0.4},
            'noise': {'positive': 0.5, 'negative': 0.5},
            'fog effect': {'positive': 0.7, 'negative': 0.3},
            'brightness adjustment': {'positive': 0.8, 'negative': 0.2},
            'reflection effect': {'positive': 0.7, 'negative': 0.3}
        }

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
