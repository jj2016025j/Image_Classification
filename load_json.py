# Random Image Prompt Generator
import json
import os

PROMPT_URL = "ai_image\prompt\data"

# Utility function to load JSON files
def load_json(file_name):
    with open(os.path.join(PROMPT_URL, file_name), "r", encoding="utf-8") as file:
        return json.load(file)

class BaseSettings:
    def __init__(self):
        data = load_json("base_settings.json")
        self.quality = data["quality"]  # 畫質
        self.resolution = data["resolution"]  # 解析度njo6ru

class MainSubject:
    def __init__(self):
        data = load_json("main_subject.json")
        self.person = data["person"]  # 人物
        self.animals = data["animals"]  # 動物
        self.objects = data["objects"]  # 物品
        self.scenes = data["scenes"]  # 場景

class CompositionAndAngle:
    def __init__(self):
        data = load_json("composition_and_angle.json")
        self.composition = data["composition"]  # 構圖
        self.angle = data["angle"]  # 角度

class Background:
    def __init__(self):
        data = load_json("background.json")
        self.nature = data["nature"]  # 自然景色
        self.city = data["city"]  # 城市景觀
        self.abstract = data["abstract"]  # 抽象
        self.fictional = data["fictional"]  # 虛構

class LightingAndColor:
    def __init__(self):
        data = load_json("lighting_and_color.json")
        self.lighting = data["lighting"]  # 光線
        self.tone = data["tone"]  # 色調
        self.filter = data["filter"]  # 濾鏡

class Style:
    def __init__(self):
        data = load_json("style.json")
        self.styles = data["styles"]  # 風格

class Atmosphere:
    def __init__(self):
        data = load_json("atmosphere.json")
        self.emotion = data["emotion"]  # 情緒
        self.festival = data["festival"]  # 節日

class ExtraElements:
    def __init__(self):
        data = load_json("extra_elements.json")
        self.text = data["text"]  # 文字
        self.borders = data["borders"]  # 邊框
        self.effects = data["effects"]  # 特效

# Usage example
if __name__ == "__main__":
    base_settings = BaseSettings()
    main_subject = MainSubject()
    composition_and_angle = CompositionAndAngle()
    background = Background()
    lighting_and_color = LightingAndColor()
    style = Style()
    atmosphere = Atmosphere()
    extra_elements = ExtraElements()

    print("Base Settings:", vars(base_settings))
    print("Main Subject:", vars(main_subject))
    print("Composition and Angle:", vars(composition_and_angle))
    print("Background:", vars(background))
    print("Lighting and Color:", vars(lighting_and_color))
    print("Style:", vars(style))
    print("Atmosphere:", vars(atmosphere))
    print("Extra Elements:", vars(extra_elements))
