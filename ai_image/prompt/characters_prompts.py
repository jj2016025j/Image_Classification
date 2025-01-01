from ai_image.prompt.character_prompts import CharacterPrompts
from ai_image.prompt.pose_prompts import PosePrompts
from ai_image.prompt.clothing_prompts import ClothingPrompts
import random
from ai_image.utils import weighted_sample

class CharactersPrompts:
    def __init__(self):
        self.characterPrompts = CharacterPrompts
        self.posePrompts = PosePrompts
        self.clothingPrompts = ClothingPrompts
        
    def generate_prompts(self):
            weighted_sample(self.character.numbers, count=1)[0]
            num_characters = random.choices(range(1, 6), weights=[0.95, 0.08, 0.01, 0.007, 0.003], k=1)[0]
            prompts = [self.generate_character() for _ in range(num_characters)]
            return [item for sublist in prompts for item in sublist]

# 測試程式
if __name__ == "__main__":
    character_prompts = CharacterPrompts()

    result = character_prompts.generate_prompts()
    print("隨機生成多個角色提示詞:", result)
