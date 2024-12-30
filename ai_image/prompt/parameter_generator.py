import random
from ai_image.prompt.data.composition_and_angle import CompositionPrompts, EffectsPrompts, PerspectivePrompts
from ai_image.prompt.data.image_style import ImageStyle
from ai_image.prompt.data.imgae_quality import ImageSettings
from ai_image.prompt.data.parameters import *

# 隨機選擇圖片品質和效果
def generate_random_picture():
    return [
        ImageSettings().generate_combined_list(mode='positive', count=20),
        ImageStyle().get_image_style(),
        PerspectivePrompts().generate_prompt(count=1),
        CompositionPrompts().generate_prompt(count=1),
        EffectsPrompts().generate_prompt(count=3)
    ]

# 隨機選擇外觀和角色
def generate_random_appearance():
    return [
        random.choice(人数),
        random.choice(age),
        random.choice(gender),
        random.choice(roles_and_jobs),
        random.choice(skin_tone),
        random.choice(body_type),
        random.choice(facial_features['eyebrows']),
        random.choice(facial_features['eye_color']),
        random.choice(facial_features['mouth']),
        random.choice(facial_features['ears']),
        random.choice(facial_features['beard']),
        random.choice(facial_features['teeth']),
        random.choice(hair['length']),
        random.choice(hair['color']),
        random.choice(hair['bangs']),
        random.choice(hair['braids']),
        random.choice(hair['style']),
        random.choice(upper_body['chest']),
        random.choice(upper_body['waist']),
        random.choice(upper_body['back']),
        random.choice(lower_body['butt']),
        random.choice(lower_body['legs']),
        random.choice(lower_body['feet']),
        random.choice(tail),
        random.choice(wings),
        random.choice(horns)
    ]

# 隨機選擇服裝
def generate_random_clothing():
    return [
        random.choice(full_body_clothing),
        random.choice(clothing_style),
        random.choice(accessories),
        random.choice(head_accessories),
        random.choice(upper_body_accessories),
        random.choice(lower_body_accessories)
    ]

# 隨機選擇姿勢
def generate_random_pose():
    return [
        random.choice(poses['action']),
        random.choice(poses['gaze']),
        random.choice(poses['expression']),
        random.choice(poses['emotion']),
        random.choice(poses['upper_body']),
        random.choice(poses['lower_body'])
    ]

# 隨機選擇環境
def generate_random_environment():
    return [
        random.choice(seasons),
        random.choice(atmosphere),
        random.choice(lighting),
        random.choice(outdoor),
        random.choice(indoor)
    ]

# 生成完整的隨機提示詞
def generate_parameters():
    prompt = []
    prompt += generate_random_picture()
    prompt += generate_random_appearance()
    prompt += generate_random_clothing()
    prompt += generate_random_pose()
    prompt += generate_random_environment()
    return prompt

def get_parameters():
    random_parameters = generate_parameters()
    parameters_string = ', '.join(map(str, random_parameters))
    print('parameters:' + parameters_string + '\n')

    return parameters_string

# 調用並打印結
def main():
    parameters_string = get_parameters()
    print(parameters_string)

if __name__ == '__main__':
    main()