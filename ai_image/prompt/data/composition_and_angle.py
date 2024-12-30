import random

def weighted_sample(option_dict, count=1):
    keys = list(option_dict.keys())
    weights = list(option_dict.values())
    selected_items = []
    while len(selected_items) < min(count, len(keys)):
        choice = random.choices(population=keys, weights=weights, k=1)[0]
        if choice not in selected_items:
            selected_items.append(choice)
    return selected_items

class PerspectivePrompts:
    def __init__(self):
        # 視角提示詞與權重
        self.prompts = {
            'bird\'s eye view': 0.9,  # 鳥瞰視角
            'scorpion view': 0.5,  # 蠍子視角
            'top-down view': 0.9,  # 俯視角
            'low angle': 0.8,  # 低視角
            'side angle': 0.8,  # 側視角
            'front view': 0.9,  # 正面視角
            'close-up': 0.9,  # 特寫
            'face-close-up': 0.9,  # 近距離特寫
            'long shot': 0.7,  # 遠距離視角
            'zoom out': 0.6,  # 鏡頭拉遠
            'close up portrait': 0.9,  # 特寫肖像
            'dutch angle': 0.7,  # 荷蘭角
            'focused view': 0.8  # 焦點集中
        }

    def generate_prompt(self, count=1):
        return weighted_sample(self.prompts, count)
      
class CompositionPrompts:
    def __init__(self):
        # 構圖提示詞與權重
        self.prompts = {
            'central composition': 0.9,  # 中心構圖
            'diagonal composition': 0.8,  # 對角構圖
            'golden ratio': 0.9,  # 黃金分割構圖
            'rule of thirds': 0.9,  # 三分法構圖
            'symmetrical composition': 0.7,  # 對稱構圖
            'asymmetrical composition': 0.7,  # 非對稱構圖
            'framed composition': 0.6,  # 框架構圖
            'leading lines': 0.8,  # 引導線構圖
            'minimal composition': 0.5,  # 簡約構圖
            'Half-body': 0.4,  # 半身
            'Full-body': 0.5,  # 全身
            'complex composition': 0.4  # 複雜構圖
        }

    def generate_prompt(self, count=1):
        return weighted_sample(self.prompts, count)
      
class EffectsPrompts:
    def __init__(self):
        # 效果提示詞與權重
        self.prompts = {
            'blur': 0.6,  # 模糊
            'texture': 0.8,  # 紋理
            'highlights': 0.9,  # 高光
            'shadows': 0.9,  # 陰影
            'filter': 0.7,  # 濾鏡
            'vintage effect': 0.6,  # 復古效果
            'glow': 0.8,  # 光暈
            'gradient effect': 0.5,  # 漸變效果
            'distortion': 0.4,  # 失真效果
            'refraction effect': 0.6,  # 折射效果
            'noise': 0.5,  # 雜訊
            'fog effect': 0.7,  # 霧化
            'brightness adjustment': 0.8,  # 亮度調整
            'reflection effect': 0.7  # 反射效果
        }

    def generate_prompt(self, count=3):
        return weighted_sample(self.prompts, count)
      
            
# 測試程式
if __name__ == "__main__":
    perspective = PerspectivePrompts()
    composition = CompositionPrompts()
    effects = EffectsPrompts()

    perspective_prompt = perspective.generate_prompt(count=1)
    composition_prompt = composition.generate_prompt(count=1)
    effects_prompt = effects.generate_prompt(count=3)

    print("視角提示詞:", perspective_prompt)
    print("構圖提示詞:", composition_prompt)
    print("效果提示詞:", effects_prompt)
