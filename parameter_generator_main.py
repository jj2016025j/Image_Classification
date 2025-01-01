# 調用並打印
from ai_image.prompt.character_prompts import CharacterPrompts
from ai_image.prompt.clothing_prompts import ClothingPrompts
from ai_image.prompt.parameter_generator import generate_parameters
from ai_image.prompt.pose_prompts import PosePrompts

if __name__ == '__main__':
    character_prompts = CharacterPrompts()
    # print(f"角色基本設定: {character_prompts.generate_prompts(mode='positive')}\n")
    
    pose_prompts = PosePrompts()
    # print(f"姿勢動作: {pose_prompts.generate_prompts(mode='positive')}\n")
    
    clothing_prompts = ClothingPrompts()
    # print(f"外觀裝飾: {clothing_prompts.generate_prompts(mode='positive')}\n")
    
    print(f"正面 Prompt: {generate_parameters(mode='positive')}\n")
    print(f"負面 Prompt: {generate_parameters(mode='negative')}\n")     