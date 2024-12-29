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

class PositivePrompts:
    class BasicSettings:
        class Composition:
            def __init__(self):
                self.options = [
                    "close-up",  # 特寫
                    "half-body",  # 半身像
                    "full-body",  # 全身像
                    "group shot",  # 群體合照
                    "dynamic composition"  # 動態構圖
                ]

        class Angle:
            def __init__(self):
                self.options = [
                    "high angle",  # 高角度
                    "low angle",  # 低角度
                    "front view",  # 正面視角
                    "side view",  # 側面視角
                    "back view",  # 背面視角
                    "from above",  # 從上方
                    "from below",  # 從下方
                    "dutch angle"  # 傾斜角度
                ]

        def __init__(self):
            self.composition = self.Composition()
            self.angle = self.Angle()

    class StyleSettings:
        class Lighting:
            def __init__(self):
                self.options = [
                    "natural lighting",  # 自然光
                    "soft light",  # 柔光
                    "hard light",  # 硬光
                    "backlight",  # 逆光
                    "candlelight",  # 蠟燭光
                    "volumetric lighting",  # 體積光
                    "dynamic lighting"  # 動態光線
                ]

        class Tone:
            def __init__(self):
                self.options = [
                    "warm tones",  # 暖色調
                    "cool tones",  # 冷色調
                    "high contrast",  # 高對比
                    "pastel tones",  # 粉彩色調
                    "monochrome",  # 單色
                    "gradient tones"  # 漸變色調
                ]

        class Filter:
            def __init__(self):
                self.options = [
                    "HDR",  # 高動態範圍
                    "vintage",  # 復古
                    "black and white",  # 黑白
                    "color boost",  # 色彩增強
                    "soft glow"  # 柔光濾鏡
                ]

        def __init__(self):
            self.lighting = self.Lighting()
            self.tone = self.Tone()
            self.filter = self.Filter()

    class SubjectSettings:
        class Features:
            def __init__(self):
                self.options = [
                    "slender",  # 苗條
                    "plump",  # 豐滿
                    "fit",  # 健壯
                    "tall",  # 高挑
                    "petite",  # 嬌小
                    "muscular"  # 肌肉發達
                ]

        class Age:
            def __init__(self):
                self.options = [
                    "young",  # 年輕
                    "adult",  # 成年
                    "middle-aged",  # 中年
                    "elderly",  # 老年
                    "child"  # 兒童
                ]

        class Gender:
            def __init__(self):
                self.options = [
                    "female",  # 女性
                    "male",  # 男性
                    "androgynous"  # 中性
                ]

        class Clothing:
            def __init__(self):
                self.options = [
                    "formal wear",  # 正裝
                    "casual wear",  # 休閒裝
                    "sportswear",  # 運動服
                    "swimwear",  # 泳裝
                    "uniform",  # 制服
                    "gown",  # 禮服
                    "lingerie",  # 內衣
                    "traditional attire"  # 傳統服飾
                ]

        class Accessories:
            def __init__(self):
                self.options = [
                    "necklace",  # 項鍊
                    "earrings",  # 耳環
                    "bracelet",  # 手鐲
                    "watch",  # 手錶
                    "hair ornament",  # 髮飾
                    "choker"  # 項圈
                ]

        class BodyParts:
            class Head:
                class Face:
                    def __init__(self):
                        self.options = [
                            "smiling",  # 微笑
                            "shy",  # 害羞
                            "crying",  # 哭泣
                            "surprised",  # 驚訝
                            "sad",  # 悲傷
                            "joyful"  # 喜悅
                        ]

                class Hair:
                    def __init__(self):
                        self.options = [
                            "long hair",  # 長髮
                            "short hair",  # 短髮
                            "medium hair",  # 中長髮
                            "blonde",  # 金髮
                            "brown",  # 棕髮
                            "black",  # 黑髮
                            "white",  # 白髮
                            "red",  # 紅髮
                            "wavy",  # 捲髮
                            "straight",  # 直髮
                            "ponytail",  # 馬尾
                            "braid"  # 辮子
                        ]

                def __init__(self):
                    self.face = self.Face()
                    self.hair = self.Hair()

            class Hands:
                def __init__(self):
                    self.options = [
                        "raising hand",  # 舉手
                        "fist",  # 握拳
                        "pointing"  # 指向
                    ]

            class Chest:
                def __init__(self):
                    self.options = [
                        "large breasts",  # 大胸
                        "medium breasts",  # 中胸
                        "small breasts",  # 小胸
                        "flat chest",  # 平胸
                        "cleavage"  # 乳溝
                    ]

            class Hips:
                def __init__(self):
                    self.options = [
                        "tight",  # 緊實
                        "round",  # 圓潤
                        "small"  # 小巧
                    ]

            class Legs:
                def __init__(self):
                    self.options = [
                        "long legs",  # 長腿
                        "toned legs",  # 緊實的腿
                        "slim legs",  # 修長的腿
                        "stockings"  # 長筒襪
                    ]

            def __init__(self):
                self.head = self.Head()
                self.hands = self.Hands()
                self.chest = self.Chest()
                self.hips = self.Hips()
                self.legs = self.Legs()

        def __init__(self):
            self.features = self.Features()
            self.age = self.Age()
            self.gender = self.Gender()
            self.clothing = self.Clothing()
            self.accessories = self.Accessories()
            self.body_parts = self.BodyParts()

    class Background:
        def __init__(self):
            self.options = [
                "indoors",  # 室內
                "outdoors",  # 室外
                "forest",  # 森林
                "beach",  # 海灘
                "cityscape",  # 城市景觀
                "mountains",  # 山脈
                "flower fields",  # 花田
                "gradient",  # 漸層背景
                "geometric shapes"  # 幾何圖案
            ]

    class SpecificObjects:
        def __init__(self):
            self.options = [
                "table",  # 桌子
                "chair",  # 椅子
                "bed",  # 床
                "car",  # 車輛
                "train",  # 火車
                "book",  # 書
                "cup"  # 杯子
            ]

    class VisualEffects:
        class Atmosphere:
            def __init__(self):
                self.options = [
                    "warm",  # 溫暖
                    "suspenseful",  # 緊張
                    "bright",  # 明亮
                    "dark"  # 陰暗
                ]

        class Text:
            def __init__(self):
                self.options = [
                    "add slogan",  # 添加標語
                    "add signature",  # 添加簽名
                    "no text"  # 無文字
                ]

        class Borders:
            def __init__(self):
                self.options = [
                    "no border",  # 無邊框
                    "simple border",  # 簡單邊框
                    "patterned border"  # 圖案邊框
                ]

        class Effects:
            def __init__(self):
                self.options = [
                    "fire",  # 火焰
                    "snow",  # 雪花
                    "lightning",  # 閃電
                    "halo",  # 光暈
                    "neon"  # 霓虹
                ]

        def __init__(self):
            self.atmosphere = self.Atmosphere()
            self.text = self.Text()
            self.borders = self.Borders()
            self.effects = self.Effects()

    def __init__(self):
        self.basic_settings = self.BasicSettings()
        self.style_settings = self.StyleSettings()
        self.subject_settings = self.SubjectSettings()
        self.background = self.Background()
        self.specific_objects = self.SpecificObjects()
        self.visual_effects = self.VisualEffects()
