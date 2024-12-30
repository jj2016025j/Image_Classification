from ai_image.prompt.data.background import Atmosphere, Background, Season
from ai_image.prompt.data.composition_and_angle import CompositionPrompts, EffectsPrompts, PerspectivePrompts
from ai_image.prompt.data.image_style import ImageStyle
from ai_image.prompt.data.imgae_quality import ImageSettings
from ai_image.prompt.data.lighting_and_color import FilterPrompts, LightingPrompts, TonePrompts
from ai_image.prompt.data.parameters import *
from ai_image.prompt.data.subject import CharacterPrompts

# 隨機選擇圖片品質和效果
def generate_base_prompt():
    return [
        ImageSettings().generate_combined_list(mode='positive', count=20),
        ImageStyle().get_image_style(),
        PerspectivePrompts().generate_prompt(count=1),
        CompositionPrompts().generate_prompt(count=1),
        EffectsPrompts().generate_prompt(count=3),
        LightingPrompts().generate_prompt(count=1),
        TonePrompts().generate_prompt(count=1),
        FilterPrompts().generate_prompt(count=3)
    ]

def generate_character_prompts():
     return CharacterPrompts().generate_character_prompts(),
    
   
# 隨機選擇環境
def generate_random_environment():
    return [
        Background().generate_background(theme='realistic'),
        Season().generate_season(),
        Atmosphere().generate_atmosphere(),
    ]

# 生成完整的隨機提示詞
def generate_parameters():
    prompt = []
    # print(f"基本優化:{generate_base_prompt()}\n")
    prompt += generate_base_prompt()
    
    # print(f"人物參數:{generate_character_prompts()}\n")
    prompt += generate_character_prompts()
    
    # print(f"背景環境參數:{generate_random_environment()}\n")
    # prompt += generate_random_environment()
    
    parameters_string = ', '.join(map(str, prompt))
    return parameters_string


# 調用並打印
def main():
    generate_parameters()

if __name__ == '__main__':
    main()