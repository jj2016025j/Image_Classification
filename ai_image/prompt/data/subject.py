from ai_image.prompt.data import character
from ai_image.prompt.data import pose
import random
# from ai_image.utils import weighted_sample

def weighted_sample(option_dict, count=1):
    """
    根據權重隨機選擇不重複的項目。
    :param option_dict: 包含提示詞和權重的字典。
    :param count: 選擇的項目數量。
    :return: 不重複選擇的項目列表。
    """
    keys = list(option_dict.keys())
    weights = list(option_dict.values())
    selected_items = []
    while len(selected_items) < min(count, len(keys)):
        choice = random.choices(population=keys, weights=weights, k=1)[0]
        if choice not in selected_items:
            selected_items.append(choice)
    return selected_items

class CharacterPrompts:
    def __init__(self):
        self.character = character
        self.pose = pose
        
    def generate_gender(self):
        return weighted_sample(self.character.gender, count=1)[0]

    def generate_age(self):
        return weighted_sample(self.character.age, count=1)[0]
    
    def generate_skin_tone(self):
        skin_tone = weighted_sample(self.character.skin_tone, count=1)[0]
        return f"{skin_tone} skin"

    def generate_body_type(self):
        body_type = weighted_sample(self.character.body_type, count=1)[0]
        return f"{body_type} body"
    
    def generate_facial_features(self):
        return [
            f"{weighted_sample(self.character.facial_features['eyebrows'], count=1)[0]} eyebrows",
            f"{weighted_sample(self.character.facial_features['eye_color'], count=1)[0]} eyes",
            f"{weighted_sample(self.character.facial_features['mouth'], count=1)[0]} mouth",
            f"{weighted_sample(self.character.facial_features['ears'], count=1)[0]}",
            f"{weighted_sample(self.character.facial_features['beard'], count=1)[0]}",
            f"{weighted_sample(self.character.facial_features['teeth'], count=1)[0]}"
        ]

    def generate_hair(self):
        return [
            f"{weighted_sample(self.character.hair['length'], count=1)[0]} hair",
            f"{weighted_sample(self.character.hair['color'], count=1)[0]} hair",
            f"{weighted_sample(self.character.hair['bangs'], count=1)[0]}",
            f"{weighted_sample(self.character.hair['braids'], count=1)[0]}",
            f"{weighted_sample(self.character.hair['style'], count=1)[0]}"
        ]
        
    def generate_body_details(self):
        return [
            f"{weighted_sample(self.character.body_details['chest'], count=1)[0]}",
            f"{weighted_sample(self.character.body_details['waist'], count=1)[0]}",
            f"{weighted_sample(self.character.body_details['back'], count=1)[0]}",
            f"{weighted_sample(self.character.body_details['butt'], count=1)[0]}",
            f"{weighted_sample(self.character.body_details['legs'], count=1)[0]}",
            f"{weighted_sample(self.character.body_details['feet'], count=1)[0]}"
        ]
        
    def generate_tail(self):
        return weighted_sample(self.character.tail, count=1)[0]

    def generate_wings(self):
        return weighted_sample(self.character.wings, count=1)[0]

    def generate_horns(self):
        return weighted_sample(self.character.horns, count=1)[0]
    
    # 動作生成
    def generate_action(self):
        return weighted_sample(self.pose.action, count=1)[0]

    def generate_gaze(self):
        return weighted_sample(self.pose.gaze, count=1)[0]

    def generate_expression(self):
        return weighted_sample(self.pose.expression, count=1)[0]

    def generate_emotion(self):
        return weighted_sample(self.pose.emotion, count=1)[0]

    def generate_arm_action(self):
        return weighted_sample(self.pose.arm_action, count=1)[0]

    def generate_leg_action(self):
        return weighted_sample(self.pose.leg_action, count=1)[0]
    
    def generate_character(self):
        gender = self.generate_gender()
        age = self.generate_age()
        skin_tone = self.generate_skin_tone()
        body_type = self.generate_body_type()
        facial_features = self.generate_facial_features()
        hair_features = self.generate_hair()
        body_details = self.generate_body_details()
        tail = self.generate_tail()
        wings = self.generate_wings()
        horns = self.generate_horns()
        
        action = self.generate_action()
        gaze = self.generate_gaze()
        expression = self.generate_expression()
        emotion = self.generate_emotion()
        upper_body = self.generate_arm_action()
        lower_body = self.generate_leg_action()
        
        return [
            gender,
            age,
            skin_tone,
            body_type,
            *facial_features,
            *hair_features,
            *body_details,
            tail,
            wings,
            horns,
            
            action,
            gaze,
            expression,
            emotion,
            upper_body,
            lower_body
        ]
        
    def generate_character_prompts(self):
            weighted_sample(self.character.numbers, count=1)[0]
            num_characters = random.choices(range(1, 6), weights=[0.9, 0.08, 0.01, 0.007, 0.003], k=1)[0]
            prompts = [self.generate_character() for _ in range(num_characters)]
            return [item for sublist in prompts for item in sublist]

# 測試程式
if __name__ == "__main__":
    character_prompts = CharacterPrompts()
    result = character_prompts.generate_character()
    # print("隨機生成的角色提示詞:", result)

    result = character_prompts.generate_character_prompts()
    print("隨機生成多個角色提示詞:", result)
