import random
from prompt.negatives import *
from prompt.uilte import convert_prompt_to_string

# 隨機選擇 NSFW-related restrictions
def generate_nsfw_related():
    return random.choice(nsfw_related)

# 隨機選擇 Quality-related restrictions
def generate_quality_related():
    return random.choice(quality_related)

# 隨機選擇 Art Style-related restrictions
def generate_art_style_related():
    return random.choice(art_style_related)

# 隨機選擇 Anatomy and Body-related errors
def generate_anatomy_related():
    return random.choice(anatomy_related)

# 隨機選擇 Color and Effect-related restrictions
def generate_color_related():
    return random.choice(color_related)

# 隨機選擇 Skin-related issues
def generate_skin_related():
    return random.choice(skin_related)

# 隨機選擇 Signature and Watermark
def generate_signature_related():
    return random.choice(signature_related)

# 隨機選擇 Miscellaneous issues
def generate_miscellaneous():
    return random.choice(miscellaneous)

# 生成完整的負面提示詞
def generate_negative():
    prompt = []
    prompt.append(generate_nsfw_related())
    prompt.append(generate_quality_related())
    prompt.append(generate_art_style_related())
    prompt.append(generate_anatomy_related())
    prompt.append(generate_color_related())
    prompt.append(generate_skin_related())
    prompt.append(generate_signature_related())
    prompt.append(generate_miscellaneous())
    return prompt

def get_negatives():
    random_negatives = generate_negative()
    negatives_string = convert_prompt_to_string(random_negatives)
    print('negatives:' + negatives_string + '\n')

    return negatives_string

# 調用並打印結
def main():
    negatives_string = get_negatives()
    print(negatives_string)

if __name__ == '__main__':
    main()