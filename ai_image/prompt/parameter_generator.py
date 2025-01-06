from ai_image.prompt.background import Atmosphere, Background, Season
from ai_image.prompt.composition_and_angle import CompositionPrompts, EffectsPrompts, PerspectivePrompts
from ai_image.prompt.image_style import ImageStyle
from ai_image.prompt.imgae_quality import ImageSettings
from ai_image.prompt.lighting_and_color import FilterPrompts, LightingPrompts, TonePrompts
from ai_image.prompt.data.clothing import *
from ai_image.prompt.characters_prompts import CharacterPrompts
from ai_image.utils import flatten_prompts

# 隨機選擇圖片品質和效果
def generate_base_prompt(mode='positive',):
    return [
        ImageSettings().generate_combined_list(mode=mode, count=20),
        ImageStyle().get_image_style(mode=mode, count=1),
        PerspectivePrompts().generate_prompts(mode=mode, count=1),
        CompositionPrompts().generate_prompts(mode=mode, count=1),
        EffectsPrompts().generate_prompts(mode=mode, count=3),
        LightingPrompts().generate_prompts(mode=mode, count=1),
        TonePrompts().generate_prompts(mode=mode, count=1),
        FilterPrompts().generate_prompts(mode=mode, count=3)
    ]

def generate_character_prompts(mode='positive',):
     return CharacterPrompts().generate_prompts(mode=mode,),
    
   
# 隨機選擇環境
def generate_random_environment(mode='positive',):
    return [
        Background().generate_background(mode=mode, theme='realistic'),
        Season().generate_season(mode=mode, ),
        Atmosphere().generate_atmosphere(mode=mode, ),
    ]

# 生成完整的隨機提示詞
def generate_parameters(mode='positive', ):
    prompt = []
    print(f"基本優化:{generate_base_prompt(mode=mode, )}\n")
    prompt += generate_base_prompt(mode=mode, )
    
    print(f"人物參數:{generate_character_prompts(mode=mode, )}\n")
    prompt += generate_character_prompts(mode=mode, )
    
    print(f"背景環境參數:{generate_random_environment(mode=mode, )}\n")
    prompt += generate_random_environment(mode=mode, )
    
    flat_prompt = flatten_prompts(prompt)
    parameters_string = ', '.join(map(str, flat_prompt))
    
    return parameters_string


# 調用並打印
def main():
    generate_parameters(mode='positive',)
    generate_parameters(mode='negative',)

if __name__ == '__main__':
    main()