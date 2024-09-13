import random

# 畫質、視角、風格、局部優化
image_quality = ["high resolution", "low resolution", "perfect face", "detailed texture"]
perspective = ["bird's-eye view", "first-person view", "wide angle", "close-up"]
style = ["realistic", "cartoonish", "anime style", "sketch"]
enhancements = ["perfect face", "smooth skin", "sharp details", "natural lighting"]

# 人物、性別、角色設定、人數
character_gender = ["male", "female", "androgynous"]
character_type = ["hero", "villain", "sidekick", "mysterious stranger"]
number_of_characters = ["1 character", "2 characters", "group of 3", "crowd of 5+"]

# 職業、動漫角色
profession = ["warrior", "mage", "healer", "assassin"]
anime_role = ["main protagonist", "supporting character", "antagonist"]

# 五官、表情、情緒
facial_features = ["sharp eyebrows", "large eyes", "thin lips", "pointed ears", "bushy beard", "white teeth"]
expression = ["smiling", "angry", "sad", "surprised", "neutral"]
emotion = ["joy", "fear", "anger", "disgust", "confusion"]

# 頭髮、髮飾
hair_length = ["short", "medium", "long"]
hair_color = ["black", "blonde", "red", "blue", "green"]
bangs = ["with bangs", "no bangs"]
braids = ["braided", "no braids"]
hairstyle = ["curly", "straight", "wavy"]
hair_accessories = ["ribbon", "hairpin", "headband"]

# 服裝、鞋子、帽子
upper_clothing = ["t-shirt", "armor", "robe", "jacket"]
lower_clothing = ["pants", "skirt", "shorts"]
clothing_style = ["casual", "formal", "fantasy", "futuristic"]
shoes = ["boots", "sneakers", "sandals"]
hat = ["none", "cap", "helmet"]

# 尾巴、翅膀、角
extra_features = ["tail", "wings", "horns", "none"]

# 姿勢、手勢
pose = ["standing", "sitting", "running", "flying"]
gesture = ["peace sign", "thumbs up", "pointing", "holding weapon"]

# 視線、動作
eyes_direction = ["looking forward", "looking left", "looking up", "closed eyes"]
upper_body_action = ["waving", "pointing", "holding object", "crossing arms"]
lower_body_action = ["walking", "kicking", "kneeling"]

# 環境、季節、光線、藝術風格
environment = ["forest", "city", "desert", "underwater", "space"]
season = ["spring", "summer", "autumn", "winter"]
lighting = ["sunset", "moonlight", "natural daylight", "dim"]
art_style = ["abstract", "classic painting", "modern anime", "manga style"]
magic_elements = ["fire magic", "ice magic", "wind magic", "shadow magic"]

# 背景氛圍
background_mood = ["mysterious", "cheerful", "dark", "romantic"]

# 隨機生成提示詞
def generate_prompt():
    prompt = []
    prompt.append(random.choice(image_quality))
    prompt.append(random.choice(perspective))
    prompt.append(random.choice(style))
    prompt.append(random.choice(enhancements))
    
    prompt.append(random.choice(character_gender))
    prompt.append(random.choice(character_type))
    prompt.append(random.choice(number_of_characters))
    
    prompt.append(random.choice(profession))
    prompt.append(random.choice(anime_role))
    
    prompt.append(random.choice(facial_features))
    prompt.append(random.choice(expression))
    prompt.append(random.choice(emotion))
    
    prompt.append(random.choice(hair_length))
    prompt.append(random.choice(hair_color))
    prompt.append(random.choice(bangs))
    prompt.append(random.choice(braids))
    prompt.append(random.choice(hairstyle))
    prompt.append(random.choice(hair_accessories))
    
    prompt.append(random.choice(upper_clothing))
    prompt.append(random.choice(lower_clothing))
    prompt.append(random.choice(clothing_style))
    prompt.append(random.choice(shoes))
    prompt.append(random.choice(hat))
    
    prompt.append(random.choice(extra_features))
    
    prompt.append(random.choice(pose))
    prompt.append(random.choice(gesture))
    
    prompt.append(random.choice(eyes_direction))
    prompt.append(random.choice(upper_body_action))
    prompt.append(random.choice(lower_body_action))
    
    prompt.append(random.choice(environment))
    prompt.append(random.choice(season))
    prompt.append(random.choice(lighting))
    prompt.append(random.choice(art_style))
    prompt.append(random.choice(magic_elements))
    
    prompt.append(random.choice(background_mood))
    
    return ' '.join(prompt)

# 測試生成提示詞
print(generate_prompt())

# AI繪圖提示詞的分類參數
class AIDrawingPromptCategories:
    # 圖像品質
    image_quality = ["high_resolution", "ultra_realistic", "low_poly", "pixel_art", "hand_drawn", "blurred"]
    
    # 視角與構圖
    perspective = ["bird_eye_view", "close_up", "panoramic", "wide_angle", "overhead_shot", "low_angle"]
    
    # 風格
    style = ["realistic", "illustrative", "anime_style", "misty_style", "futuristic", "steampunk", "classical"]
    
    # 人物特徵
    facial_features = ["smiling", "sad", "angry", "eye_color", "hairstyle", "skin_tone", "body_type"]
    
    # 配件與裝飾
    accessories = ["hat", "glasses", "watch", "earrings", "necklace"]
    
    # 服裝
    clothing = ["modern_clothing", "traditional_clothing", "armor", "casual_wear", "formal_wear"]
    
    # 姿勢
    posture = ["standing", "sitting", "running", "jumping", "lying_down"]
    
    # 環境
    environment = ["urban_landscape", "forest", "beach", "desert", "space"]
    
    # 光線效果
    lighting = ["soft_lighting", "high_contrast", "sunset_lighting", "neon_light", "candlelight"]
    
    # 情緒氛圍
    mood = ["warm", "cold", "creepy", "dreamy", "romantic"]

# 畫質類
局部優化詞 = [
    '細節高光', 
    '柔焦邊緣', 
    '超精細', 
    '光影效果', 
    '邊緣加強', 
    '色彩校正', 
    '對比度增強', 
    '細膩質感', 
    '陰影增強'
]

圖像品質 = [
    '高解析度', 
    '4K畫質', 
    '8K畫質', 
    '超高解析度', 
    'HDR', 
    '細膩畫質', 
    '動態範圍增強', 
    '光線追蹤效果'
]

視角 = [
    '鳥瞰視角', 
    '蠍子視角', 
    '俯視角', 
    '低視角', 
    '側視角', 
    '正面視角', 
    '近距離視角', 
    '遠距離視角', 
    '鏡頭拉遠', 
    '焦點集中'
]

影像風格 = [
    '照片寫實風格', 
    '手繪風格', 
    '動漫', 
    '二次元', 
    '3D渲染風', 
    '印象派', 
    '巴洛克', 
    '夢幻風格', 
    '新藝術風格', 
    '水彩風格', 
    '油畫風格', 
    '素描風格', 
    '漫畫風格', 
    '復古風格', 
    '像素藝術'
]

效果 = [
    '模糊', 
    '紋理', 
    '高光', 
    '陰影', 
    '濾鏡', 
    '復古效果', 
    '光暈', 
    '漸變效果', 
    '失真效果', 
    '折射效果', 
    '雜訊', 
    '霧化', 
    '亮度調整', 
    '反射效果'
]

構圖 = [
    '中心構圖', 
    '對角構圖', 
    '黃金分割構圖', 
    '三分法構圖', 
    '對稱構圖', 
    '非對稱構圖', 
    '框架構圖', 
    '引導線構圖', 
    '簡約構圖', 
    '複雜構圖'
]

# 畫質
畫質 = 局部優化詞 + 圖像品質 + 視角 + 影像風格 + 效果 + 構圖

# 人物類
年齡 = [
    '幼年', 
    '少年', 
    '青少年', 
    '青年', 
    '成熟', 
    '中年', 
    '老年', 
    '嬰兒', 
    '老少皆宜', 
    ''
]

性別 = [
    '男性', 
    '女性', 
    '中性', 
    '雙性', 
    '不確定', 
    '跨性別', 
    ''
]

人數 = [
    '單人', 
    '群體', 
    '雙人', 
    '三人', 
    '多人', 
    '隊伍', 
    '群眾', 
    ''
]

角色與職業 = [
    '英雄', 
    '反派', 
    '雌小鬼', 
    '大小姐', 
    '忍者', 
    '魔法師', 
    '科學家', 
    '聖騎士', 
    '間諜', 
    '獵人', 
    '戰士', 
    '巫師', 
    '野蠻人', 
    '學生', 
    '流浪者', 
    '王子/公主', 
    '醫生', 
    '騎士', 
    '法師', 
    '刺客', 
    '士兵', 
    '農民', 
    '商人', 
    '畫家', 
    '音樂家', 
    '作家', 
    '警察', 
    '消防員', 
    '教師', 
    '工匠', 
    '工程師', 
    '偵探', 
    '探險家', 
    '廚師', 
    '水手', 
    '飛行員', 
    ''
]

膚色 = [
    '白皙', 
    '深膚色', 
    '褐色', 
    '黃種膚色', 
    '淺膚色', 
    '青白色', 
    '古銅色', 
    '黝黑色', 
    '灰白色', 
    ''
]

體型 = [
    '瘦弱', 
    '健壯', 
    '豐滿', 
    '苗條', 
    '肌肉發達', 
    '嬌小', 
    '高大', 
    '矮胖', 
    '中等身材', 
    '巨人', 
    ''
]

# 外觀
五官 = {
    '眉毛': ['濃密', '稀疏', '修剪整齊', '彎曲', '粗壯', '纖細', ''],
    '眼睛顏色': ['藍', '綠', '褐', '黑', '灰', '金', '紫', '紅', ''],
    '嘴巴': ['微笑', '冷酷', '嘟嘴', '露齒微笑', '閉嘴', '張開嘴', ''],
    '耳朵': ['尖耳', '圓耳', '精靈耳', '動物耳', '大耳朵', '小耳朵', ''],
    '鬍子': ['粗獷', '修剪整齊', '山羊鬍', '絡腮鬍', '八字鬍', '無鬍子', ''],
    '牙齒': ['整齊', '尖牙', '獠牙', '缺牙', '潔白', '']
}

頭髮 = {
    '長度': ['短', '中', '長', '超短', '超長', '波浪狀', ''],
    '顏色': ['黑', '金', '紅', '白', '紫', '藍', '綠', '銀', '棕', ''],
    '瀏海': ['中分', '齊眉', '側分', '斜劉海', '無劉海', '蓋住眼睛', ''],
    '辮子': ['單辮', '雙辮', '麻花辮', '低辮', '高辮', '無辮子', ''],
    '髮型': ['卷髮', '直髮', '波浪髮', '短髮', '長捲髮', '馬尾', '丸子頭', '']
}

上半身 = {
    '胸部': ['平坦', '豐滿', '小', '大', '適中', ''],
    '腰部': ['纖細', '健壯', '粗壯', '苗條', '無腰', ''],
    '背部': ['光滑', '紋身', '疤痕', '翅膀痕跡', '']
}

下半身 = {
    '屁股': ['圓潤', '平坦', '豐滿', '小', '大', ''],
    '腿部': ['修長', '肌肉', '纖細', '粗壯', '短', ''],
    '腳步': ['赤足', '穿鞋', '穿靴子', '穿涼鞋', '']
}

尾巴 = ['狐尾', '龍尾', '貓尾', '狗尾', '蛇尾', '無尾巴', '']

翅膀 = ['天使翅膀', '惡魔翅膀', '蝙蝠翅膀', '鳥類翅膀', '龍翅膀', '無翅膀', '']

角 = ['獨角', '雙角', '鹿角', '羊角', '牛角', '無角', '']

# 外觀（完整）
外觀 = (
    list(五官['眉毛'] + 五官['眼睛顏色'] + 五官['嘴巴'] + 五官['耳朵'] + 五官['鬍子'] + 五官['牙齒']) +
    list(頭髮['長度'] + 頭髮['顏色'] + 頭髮['瀏海'] + 頭髮['辮子'] + 頭髮['髮型']) +
    list(上半身['胸部'] + 上半身['腰部'] + 上半身['背部']) +
    list(下半身['屁股'] + 下半身['腿部'] + 下半身['腳步']) +
    尾巴 + 翅膀 + 角
)

# 服裝
全身服裝 = [
    '戰甲', 
    '禮服', 
    '便服', 
    '運動服', 
    '和服', 
    '校服', 
    '燕尾服', 
    '連身裙', 
    '披風', 
    '盔甲', 
    '盜賊裝', 
    '西裝', 
    '武士服', 
    '晚禮服', 
    ''
]

衣服風格 = [
    '現代時尚', 
    '古典復古', 
    '朋克風', 
    '街頭風', 
    '哥德風', 
    '休閒風', 
    '運動風', 
    '高科技未來風', 
    '奇幻風', 
    '古風', 
    '軍裝風', 
    '浪漫風', 
    '中世紀風', 
    ''
]

裝飾 = [
    '刺繡', 
    '流蘇', 
    '繡花', 
    '珍珠', 
    '鑽石', 
    '金屬鏈', 
    '絲帶', 
    '徽章', 
    '水晶', 
    '鋸齒邊', 
    '裝飾羽毛', 
    '亮片', 
    ''
]

服裝 = [
    '皮衣', 
    '毛衣', 
    '外套', 
    '羽絨服', 
    '風衣', 
    '無袖背心', 
    '長袖襯衫', 
    '連帽衫', 
    '背心', 
    '無肩帶裙', 
    'T恤', 
    '針織衫', 
    '迷彩服', 
    ''
]

頭部配件 = [
    '帽子（棒球帽、皇冠）', 
    '髪飾（髮夾、髮箍）', 
    '面具', 
    '頭巾', 
    '護目鏡', 
    '頭盔', 
    '頭巾', 
    '眼鏡', 
    '貓耳', 
    '兔耳', 
    '頭花', 
    '髮帶', 
    '頭紗', 
    ''
]

上半身配件 = [
    '手飾（手套、手鐲）', 
    '項鍊', 
    '披肩', 
    '臂環', 
    '胸針', 
    '肩章', 
    '戒指', 
    '手錶', 
    ''
]

下半身配件 = [
    '鞋子（靴子、高跟鞋）', 
    '襪子（長襪、短襪）', 
    '護膝', 
    '腳鐲', 
    '鞋帶', 
    '涼鞋', 
    '軍靴', 
    '拖鞋', 
    '短靴', 
    '皮鞋', 
    '運動鞋', 
    ''
]

# 服裝（完整）
服裝類 = 全身服裝 + 衣服風格 + 裝飾 + 服裝 + 頭部配件 + 上半身配件 + 下半身配件

# 姿勢
動作 = [
    '跑步', 
    '站立', 
    '行走', 
    '跳躍', 
    '蹲下', 
    '跪姿', 
    '奔跑', 
    '奔躍', 
    '匍匐前進', 
    '俯身', 
    '趴著', 
    '飛行姿勢', 
    '踢腿', 
    '翻滾', 
    '格鬥姿勢', 
    '擁抱', 
    '抬手', 
    '握拳', 
    ''
]

視線 = [
    '正視', 
    '側視', 
    '俯視', 
    '仰視', 
    '回頭', 
    '遠視', 
    '瞇眼', 
    '凝視', 
    '瞟視', 
    '快速環顧', 
    '眼神交流', 
    ''
]

表情 = [
    '微笑', 
    '憤怒', 
    '驚訝', 
    '悲傷', 
    '開心', 
    '冷酷', 
    '害羞', 
    '困惑', 
    '冷漠', 
    '挑眉', 
    '焦慮', 
    '得意', 
    '驚恐', 
    '害怕', 
    ''
]

情緒 = [
    '愉悅', 
    '悲傷', 
    '平靜', 
    '激動', 
    '憤怒', 
    '緊張', 
    '驚喜', 
    '沮喪', 
    '滿足', 
    '焦慮', 
    '興奮', 
    '嫉妒', 
    '絕望', 
    '自信', 
    ''
]

上半身姿勢 = [
    '手勢（比讚、揮手）', 
    '交叉雙臂', 
    '雙手插腰', 
    '雙手合十', 
    '托腮', 
    '雙手抱胸', 
    '單手撐腰', 
    '單手指向前方', 
    '雙手搭肩', 
    '手持武器', 
    '雙手抓頭', 
    ''
]

下半身姿勢 = [
    '跳躍姿勢', 
    '靜止站姿', 
    '蹲姿', 
    '跨步', 
    '踢腿', 
    '跪姿', 
    '單腳站立', 
    '雙腳平行站立', 
    '轉身準備動作', 
    '步伐輕盈', 
    '雙腿交叉', 
    ''
]

# 姿勢（完整）
姿勢類 = 動作 + 視線 + 表情 + 情緒 + 上半身姿勢 + 下半身姿勢

# 環境類
# 環境類
季節 = [
    '春', 
    '夏', 
    '秋', 
    '冬', 
    '雨季', 
    '乾季', 
    '雪季', 
    '颱風季', 
    '初春', 
    '深秋', 
    '寒冬', 
    ''
]

氛圍 = [
    '溫暖', 
    '陰森', 
    '浪漫', 
    '悲涼', 
    '神秘', 
    '輕鬆', 
    '恐怖', 
    '緊張', 
    '荒涼', 
    '祥和', 
    '奇幻', 
    '未來感', 
    '超現實', 
    '古典', 
    ''
]

光線效果 = [
    '背光', 
    '逆光', 
    '強光', 
    '柔光', 
    '月光', 
    '燭光', 
    '星光', 
    '霧霾光', 
    '陰影覆蓋', 
    '陽光直射', 
    '黃昏光', 
    '晨光', 
    '閃電光', 
    ''
]

室外 = [
    '高樓大廈', 
    '鄉村小屋', 
    '森林', 
    '沙漠', 
    '海邊', 
    '山脈', 
    '花園', 
    '公園', 
    '城堡', 
    '湖泊', 
    '河流', 
    '草原', 
    '市中心', 
    '古老街道', 
    '瀑布', 
    '樹林小徑', 
    '田野', 
    ''
]

室內 = [
    '房間佈置（簡約、華麗）', 
    '家具（沙發、書架）', 
    '廚房', 
    '浴室', 
    '書房', 
    '臥室', 
    '客廳', 
    '餐廳', 
    '辦公室', 
    '工作室', 
    '地下室', 
    '閣樓', 
    '豪華宮殿', 
    '古董店', 
    '實驗室', 
    '大廳', 
    '教堂', 
    ''
]

# 環境（完整）
環境 = 季節 + 氛圍 + 光線效果 + 室外 + 室內

