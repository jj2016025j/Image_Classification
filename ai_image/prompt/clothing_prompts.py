from ai_image.prompt.data.clothing import Clothing, Accessories
from ai_image.utils import weighted_sample

class ClothingPrompts:
    def __init__(self):
        self.clothing = Clothing
        self.accessories = Accessories

    def generate_full_body(self, mode='positive'):
        """生成全身服裝提示"""
        return weighted_sample(self.clothing.full_body, count=1, mode=mode)[0]

    def generate_style(self, mode='positive'):
        """生成服裝風格提示"""
        return weighted_sample(self.clothing.style, count=1, mode=mode)[0]

    def generate_accessory(self, mode='positive'):
        """生成配件提示"""
        return weighted_sample(self.clothing.accessories, count=1, mode=mode)[0]

    def generate_head_accessory(self, mode='positive'):
        """生成頭部配件提示"""
        return weighted_sample(self.accessories.head, count=1, mode=mode)[0]

    def generate_upper_body_accessory(self, mode='positive'):
        """生成上半身配件提示"""
        return weighted_sample(self.accessories.upper_body, count=1, mode=mode)[0]

    def generate_lower_body_accessory(self, mode='positive'):
        """生成下半身配件提示"""
        return weighted_sample(self.accessories.lower_body, count=1, mode=mode)[0]

    def generate_prompts(self, mode='positive'):
        """整合服飾提示"""
        return [
            self.generate_full_body(mode=mode),
            self.generate_style(mode=mode),
            self.generate_accessory(mode=mode),
            self.generate_head_accessory(mode=mode),
            self.generate_upper_body_accessory(mode=mode),
            self.generate_lower_body_accessory(mode=mode),
        ]

# 測試生成提示詞
if __name__ == "__main__":
    clothing_prompts = ClothingPrompts()
    print("Clothing Prompt:", clothing_prompts.generate_prompts())
        
        
        
        
        
        
        
        

# roles_and_jobs = [  # 角色與職業
#     'hero',  # 英雄
#     'villain',  # 反派
#     'ninja',  # 忍者
#     'mage',  # 法師
#     'warrior',  # 戰士
#     'doctor',  # 醫生
#     'scientist',  # 科學家
#     'knight',  # 騎士
#     'spy',  # 間諜
#     'hunter',  # 獵人
#     'barbarian',  # 野蠻人
#     'student',  # 學生
#     'wanderer',  # 流浪者
#     'prince',  # 王子
#     'princess',  # 公主
#     'artist',  # 畫家
#     'musician',  # 音樂家
#     'writer',  # 作家
#     'police',  # 警察
#     'firefighter',  # 消防員
#     'teacher',  # 教師
#     'engineer',  # 工程師
#     'detective',  # 偵探
#     'explorer',  # 探險家
#     'chef',  # 廚師
#     'pilot',  # 飛行員
#     None
# ]