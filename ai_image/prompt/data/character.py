# ai_image\prompt\data\character.py

class Character:
    """角色相關屬性與權重"""

    # 單人或多角色類型
    numbers = {
        'solo': {'positive': 0.9, 'negative': 0.1},  # 單人
        'group': {'positive': 0.08, 'negative': 0.92},  # 群體
        'duo': {'positive': 0.01, 'negative': 0.99},  # 雙人
        'trio': {'positive': 0.007, 'negative': 0.993},  # 三人
        'multiple people': {'positive': 0.003, 'negative': 0.997},  # 多人
        'team': {'positive': 0.001, 'negative': 0.999}  # 隊伍
    }

    # 性別屬性
    gender = {
        'male': {'positive': 0.2, 'negative': 0.8},  # 男性
        'female': {'positive': 0.9, 'negative': 0.1},  # 女性
        'non-binary': {'positive': 0.3, 'negative': 0.7},  # 非二元
        'androgynous': {'positive': 0.2, 'negative': 0.8},  # 雌雄同體
        'unspecified': {'positive': 0.1, 'negative': 0.9},  # 未指定
        'transgender': {'positive': 0.2, 'negative': 0.8},  # 跨性別
    }

    # 年齡屬性
    age = {
        'child': {'positive': 0.3, 'negative': 0.7},  # 小孩
        'teen': {'positive': 0.5, 'negative': 0.5},  # 青少年
        'young adult': {'positive': 0.8, 'negative': 0.2},  # 年輕人
        'adult': {'positive': 0.7, 'negative': 0.3},  # 成年人
        'mature': {'positive': 0.6, 'negative': 0.4},  # 成熟
        'middle-aged': {'positive': 0.4, 'negative': 0.6},  # 中年
        'elderly': {'positive': 0.3, 'negative': 0.7},  # 老年
        'baby': {'positive': 0.2, 'negative': 0.8},  # 嬰兒
        'all ages': {'positive': 0.1, 'negative': 0.9},  # 所有年齡
    }

    # 膚色屬性
    skin_tone = {
        'fair': {'positive': 0.8, 'negative': 0.2},  # 白皙
        'dark': {'positive': 0.7, 'negative': 0.3},  # 深色
        'tan': {'positive': 0.6, 'negative': 0.4},  # 古銅色
        'yellow': {'positive': 0.7, 'negative': 0.3},  # 黃色
        'light': {'positive': 0.6, 'negative': 0.4},  # 淺色
        'pale': {'positive': 0.5, 'negative': 0.5},  # 蒼白
        'bronze': {'positive': 0.4, 'negative': 0.6},  # 銅色
        'black': {'positive': 0.3, 'negative': 0.7},  # 黑色
        'grey': {'positive': 0.2, 'negative': 0.8}  # 灰色
    }

    # 體型屬性
    body_type = {
        'slim': {'positive': 0.8, 'negative': 0.2},  # 苗條
        'muscular': {'positive': 0.7, 'negative': 0.3},  # 肌肉發達
        'curvy': {'positive': 0.6, 'negative': 0.4},  # 曲線美
        'petite': {'positive': 0.5, 'negative': 0.5},  # 嬌小
        'tall': {'positive': 0.7, 'negative': 0.3},  # 高挑
        'short': {'positive': 0.5, 'negative': 0.5},  # 矮小
        'medium build': {'positive': 0.6, 'negative': 0.4},  # 中等身材
        'giant': {'positive': 0.4, 'negative': 0.6},  # 巨型
        'pregnant': {'positive': 0.2, 'negative': 0.8}  # 懷孕
    }

    # 五官屬性
    facial_features = {
        'eyebrows': {
            'thick': {'positive': 0.8, 'negative': 0.2},  # 濃眉
            'thin': {'positive': 0.7, 'negative': 0.3},  # 細眉
            'well-groomed': {'positive': 0.6, 'negative': 0.4},  # 修整眉
            'arched': {'positive': 0.5, 'negative': 0.5},  # 弧形眉
            'bushy': {'positive': 0.4, 'negative': 0.6},  # 濃密眉
            'delicate': {'positive': 0.3, 'negative': 0.7},  # 精緻眉
        },
        'eye_color': {
            'blue': {'positive': 0.8, 'negative': 0.2},  # 藍色眼睛
            'green': {'positive': 0.7, 'negative': 0.3},  # 綠色眼睛
            'brown': {'positive': 0.6, 'negative': 0.4},  # 棕色眼睛
            'black': {'positive': 0.5, 'negative': 0.5},  # 黑色眼睛
            'grey': {'positive': 0.4, 'negative': 0.6},  # 灰色眼睛
            'gold': {'positive': 0.3, 'negative': 0.7},  # 金色眼睛
            'purple': {'positive': 0.2, 'negative': 0.8},  # 紫色眼睛
            'red': {'positive': 0.1, 'negative': 0.9},  # 紅色眼睛
        },
        'mouth': {
            'smile': {'positive': 0.7, 'negative': 0.3},  # 微笑
            'grim': {'positive': 0.6, 'negative': 0.4},  # 嚴肅
            'pout': {'positive': 0.5, 'negative': 0.5},  # 嘟嘴
            'wide smile': {'positive': 0.4, 'negative': 0.6},  # 開懷大笑
            'closed': {'positive': 0.3, 'negative': 0.7},  # 閉嘴
            'open': {'positive': 0.2, 'negative': 0.8},  # 開口
        },
        'ears': {
            'pointed': {'positive': 0.5, 'negative': 0.5},  # 尖耳
            'round': {'positive': 0.5, 'negative': 0.5},  # 圓耳
            'elf ears': {'positive': 0.4, 'negative': 0.6},  # 精靈耳
            'animal ears': {'positive': 0.3, 'negative': 0.7},  # 動物耳
            'large ears': {'positive': 0.2, 'negative': 0.8},  # 大耳
            'small ears': {'positive': 0.1, 'negative': 0.9},  # 小耳
        },
        'beard': {
            'rough': {'positive': 0.4, 'negative': 0.6},  # 鬍渣
            'well-trimmed': {'positive': 0.3, 'negative': 0.7},  # 修整鬍
            'goatee': {'positive': 0.2, 'negative': 0.8},  # 山羊鬍
            'full beard': {'positive': 0.3, 'negative': 0.7},  # 全鬍
            'mustache': {'positive': 0.2, 'negative': 0.8},  # 八字鬍
            'no beard': {'positive': 0.6, 'negative': 0.4},  # 無鬍
        },
        'teeth': {
            'straight': {'positive': 0.6, 'negative': 0.4},  # 整齊牙齒
            'sharp': {'positive': 0.5, 'negative': 0.5},  # 鋒利牙齒
            'fangs': {'positive': 0.4, 'negative': 0.6},  # 尖牙
            'missing teeth': {'positive': 0.3, 'negative': 0.7},  # 缺牙
            'white teeth': {'positive': 0.7, 'negative': 0.3},  # 白牙
        }
    }

    # 頭髮屬性
    hair = {
        'length': {
            'short': {'positive': 0.5, 'negative': 0.5},  # 短髮
            'medium': {'positive': 0.6, 'negative': 0.4},  # 中長髮
            'long': {'positive': 0.7, 'negative': 0.3},  # 長髮
            'extra short': {'positive': 0.4, 'negative': 0.6},  # 超短髮
            'extra long': {'positive': 0.3, 'negative': 0.7},  # 超長髮
        },
        'color': {
            'black': {'positive': 0.7, 'negative': 0.3},  # 黑色
            'gold': {'positive': 0.6, 'negative': 0.4},  # 金色
            'red': {'positive': 0.5, 'negative': 0.5},  # 紅色
            'white': {'positive': 0.4, 'negative': 0.6},  # 白色
            'purple': {'positive': 0.3, 'negative': 0.7},  # 紫色
            'blue': {'positive': 0.2, 'negative': 0.8},  # 藍色
            'green': {'positive': 0.1, 'negative': 0.9},  # 綠色
            'silver': {'positive': 0.2, 'negative': 0.8},  # 銀色
            'brown': {'positive': 0.6, 'negative': 0.4},  # 棕色
        },
        'bangs': {
            'middle part': {'positive': 0.5, 'negative': 0.5},  # 中分瀏海
            'straight bangs': {'positive': 0.4, 'negative': 0.6},  # 平瀏海
            'side bangs': {'positive': 0.3, 'negative': 0.7},  # 側瀏海
            'no bangs': {'positive': 0.6, 'negative': 0.4},  # 無瀏海
        },
        'braids': {
            'single braid': {'positive': 0.4, 'negative': 0.6},  # 單辮
            'double braids': {'positive': 0.3, 'negative': 0.7},  # 雙辮
            'loose braids': {'positive': 0.5, 'negative': 0.5},  # 鬆散辮
            'no braids': {'positive': 0.7, 'negative': 0.3},  # 無辮子
        },
        'style': {
            'curly': {'positive': 0.5, 'negative': 0.5},  # 捲髮
            'straight': {'positive': 0.6, 'negative': 0.4},  # 直髮
            'wavy': {'positive': 0.7, 'negative': 0.3},  # 波浪髮
            'ponytail': {'positive': 0.4, 'negative': 0.6},  # 馬尾
            'bun': {'positive': 0.3, 'negative': 0.7},  # 髮髻
        }
    }

    # 身體細節屬性
    body_details = {
        'chest': {
            'flat': {'positive': 0.5, 'negative': 0.5},  # 平胸
            'full': {'positive': 0.6, 'negative': 0.4},  # 豐滿
            'small': {'positive': 0.5, 'negative': 0.5},  # 小胸
            'large': {'positive': 0.4, 'negative': 0.6},  # 大胸
            'average': {'positive': 0.7, 'negative': 0.3},  # 普通胸
        },
        'waist': {
            'slim': {'positive': 0.6, 'negative': 0.4},  # 細腰
            'muscular': {'positive': 0.5, 'negative': 0.5},  # 健壯腰部
            'thick': {'positive': 0.4, 'negative': 0.6},  # 粗腰
            'petite': {'positive': 0.3, 'negative': 0.7},  # 小腰
            'no waist': {'positive': 0.2, 'negative': 0.8},  # 無腰
        },
        'back': {
            'smooth': {'positive': 0.5, 'negative': 0.5},  # 光滑背部
            'tattoos': {'positive': 0.4, 'negative': 0.6},  # 紋身
            'scars': {'positive': 0.3, 'negative': 0.7},  # 疤痕
            'wings': {'positive': 0.2, 'negative': 0.8},  # 翅膀
        },
        'butt': {
            'round': {'positive': 0.6, 'negative': 0.4},  # 圓臀
            'flat': {'positive': 0.5, 'negative': 0.5},  # 扁臀
            'full': {'positive': 0.4, 'negative': 0.6},  # 豐滿臀
            'small': {'positive': 0.3, 'negative': 0.7},  # 小臀
            'large': {'positive': 0.2, 'negative': 0.8},  # 大臀
        },
        'legs': {
            'long': {'positive': 0.5, 'negative': 0.5},  # 長腿
            'muscular': {'positive': 0.4, 'negative': 0.6},  # 肌肉腿
            'slender': {'positive': 0.6, 'negative': 0.4},  # 修長腿
            'thick': {'positive': 0.3, 'negative': 0.7},  # 粗腿
            'short': {'positive': 0.2, 'negative': 0.8},  # 短腿
        },
        'feet': {
            'barefoot': {'positive': 0.4, 'negative': 0.6},  # 赤腳
            'wearing shoes': {'positive': 0.5, 'negative': 0.5},  # 穿鞋
            'wearing boots': {'positive': 0.6, 'negative': 0.4},  # 穿靴
            'wearing sandals': {'positive': 0.3, 'negative': 0.7},  # 穿涼鞋
        }
    }

    # 尾巴屬性
    tail = {
        'fox tail': {'positive': 0.6, 'negative': 0.4},  # 狐狸尾巴
        'dragon tail': {'positive': 0.5, 'negative': 0.5},  # 龍尾
        'cat tail': {'positive': 0.4, 'negative': 0.6},  # 貓尾
        'dog tail': {'positive': 0.3, 'negative': 0.7},  # 狗尾
        'snake tail': {'positive': 0.2, 'negative': 0.8},  # 蛇尾
        'no tail': {'positive': 0.7, 'negative': 0.3},  # 無尾巴
    }   
    
    # 翅膀屬性
    wings = {
        'angel wings': {'positive': 0.6, 'negative': 0.4},  # 天使翅膀
        'demon wings': {'positive': 0.5, 'negative': 0.5},  # 惡魔翅膀
        'bat wings': {'positive': 0.4, 'negative': 0.6},  # 蝙蝠翅膀
        'bird wings': {'positive': 0.3, 'negative': 0.7},  # 鳥類翅膀
        'dragon wings': {'positive': 0.2, 'negative': 0.8},  # 龍翅膀
        'no wings': {'positive': 0.7, 'negative': 0.3},  # 無翅膀
    }

    # 角屬性
    horns = {
        'single horn': {'positive': 0.4, 'negative': 0.6},  # 單角
        'double horns': {'positive': 0.5, 'negative': 0.5},  # 雙角
        'antlers': {'positive': 0.6, 'negative': 0.4},  # 鹿角
        'ram horns': {'positive': 0.3, 'negative': 0.7},  # 公羊角
        'bull horns': {'positive': 0.2, 'negative': 0.8},  # 牛角
        'no horns': {'positive': 0.7, 'negative': 0.3},  # 無角
    }
