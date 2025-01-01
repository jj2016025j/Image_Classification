from ai_image.prompt.data.character import Character
from ai_image.utils import weighted_sample

class CharacterPrompts:
    def __init__(self):
        self.character = Character

    def generate_gender(self, mode='positive'):
        return weighted_sample(self.character.gender, count=1, mode=mode)[0]

    def generate_age(self, mode='positive'):
        return weighted_sample(self.character.age, count=1, mode=mode)[0]

    def generate_skin_tone(self, mode='positive'):
        skin_tone = weighted_sample(self.character.skin_tone, count=1, mode=mode)[0]
        return f"{skin_tone} skin"

    def generate_body_type(self, mode='positive'):
        body_type = weighted_sample(self.character.body_type, count=1, mode=mode)[0]
        return f"{body_type} body"

    def generate_facial_features(self, mode='positive'):
        return [
            f"{weighted_sample(self.character.facial_features['eyebrows'], count=1, mode=mode)[0]} eyebrows",
            f"{weighted_sample(self.character.facial_features['eye_color'], count=1, mode=mode)[0]} eyes",
            f"{weighted_sample(self.character.facial_features['mouth'], count=1, mode=mode)[0]} mouth",
            f"{weighted_sample(self.character.facial_features['ears'], count=1, mode=mode)[0]}",
            f"{weighted_sample(self.character.facial_features['beard'], count=1, mode=mode)[0]}",
            f"{weighted_sample(self.character.facial_features['teeth'], count=1, mode=mode)[0]}"
        ]

    def generate_hair(self, mode='positive'):
        return [
            f"{weighted_sample(self.character.hair['length'], count=1, mode=mode)[0]} hair",
            f"{weighted_sample(self.character.hair['color'], count=1, mode=mode)[0]} hair",
            f"{weighted_sample(self.character.hair['bangs'], count=1, mode=mode)[0]}",
            f"{weighted_sample(self.character.hair['braids'], count=1, mode=mode)[0]}",
            f"{weighted_sample(self.character.hair['style'], count=1, mode=mode)[0]}"
        ]

    def generate_body_details(self, mode='positive'):
        return [
            f"{weighted_sample(self.character.body_details['chest'], count=1, mode=mode)[0]}",
            f"{weighted_sample(self.character.body_details['waist'], count=1, mode=mode)[0]}",
            f"{weighted_sample(self.character.body_details['back'], count=1, mode=mode)[0]}",
            f"{weighted_sample(self.character.body_details['butt'], count=1, mode=mode)[0]}",
            f"{weighted_sample(self.character.body_details['legs'], count=1, mode=mode)[0]}",
            f"{weighted_sample(self.character.body_details['feet'], count=1, mode=mode)[0]}"
        ]

    def generate_prompts(self, mode='positive'):
        return [
            self.generate_gender(mode=mode),
            self.generate_age(mode=mode),
            self.generate_skin_tone(mode=mode),
            self.generate_body_type(mode=mode),
            *self.generate_facial_features(mode=mode),
            *self.generate_hair(mode=mode),
            *self.generate_body_details(mode=mode),
        ]
    
# 測試生成提示詞
if __name__ == "__main__":
    character_prompts = CharacterPrompts()
    print("Character Gender:", character_prompts.generate_prompts(mode='positive'))
