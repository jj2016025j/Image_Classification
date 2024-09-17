# Picture quality (畫質類)
image_quality = [  # 圖像品質
    'masterpiece',  # 大師作品
    'best quality',  # 最高畫質
    '4K quality',  # 4K畫質
    '8K quality',  # 8K畫質
    'high resolution',  # 高解析度
    'super high resolution',  # 超高解析度
    'highres',  # 高分辨率
    'HDR',  # HDR
    'delicate quality',  # 細膩畫質
    'enhanced dynamic range',  # 動態範圍增強
    'ray tracing effect'  # 光線追蹤效果
    'ultra-detailed'  # 超詳細
    'ray tracing effect'  # 光線追蹤效果
    'ray tracing effect'  # 光線追蹤效果
    'ray tracing effect'  # 光線追蹤效果
]

image_style = [  # 影像風格
    'photo realistic',  # 照片寫實風格
    'hand-drawn style',  # 手繪風格
    'CG', # CG
    'artbook', # 藝術書
    'illustration', # 插圖
    'fantasy', # 幻想
    'artbook', # 藝術書
    'artbook', # 藝術書
    'anime',  # 動漫
    'anime coloring', # 動畫著色
    '2D',  # 二次元
    '3D rendering style',  # 3D渲染風
    'impressionism',  # 印象派
    'baroque',  # 巴洛克
    'fantasy style',  # 夢幻風格
    'art nouveau',  # 新藝術風格
    'watercolor style',  # 水彩風格
    'oil painting style',  # 油畫風格
    'sketch style',  # 素描風格
    'comic style',  # 漫畫風格
    'retro style',  # 復古風格
    'pixel art'  # 像素藝術
]

local_enhancements = [  # 局部優化詞
    'detailed highlights',  # 細節高光
    'soft focus edges',  # 柔焦邊緣
    'ultra-fine details',  # 超精細
    'lighting effects',  # 光影效果
    'edge enhancement',  # 邊緣加強
    'color correction',  # 色彩校正
    'contrast enhancement',  # 對比度增強
    'delicate texture',  # 細膩質感
    'shadow enhancement'  # 陰影增強
]

perspective = [  # 視角
    'bird\'s eye view',  # 鳥瞰視角
    'scorpion view',  # 蠍子視角
    'top-down view',  # 俯視角
    'low angle',  # 低視角
    'side angle',  # 側視角
    'front view',  # 正面視角
    'close-up',  # 特寫
    'face-close-up',  # 近距離特寫
    'long shot',  # 遠距離視角
    'zoom out',  # 鏡頭拉遠
    'close up portrait',  # 特寫肖像
    'dutch angle',  # 荷蘭角
    'focused view'  # 焦點集中
]

effects = [  # 效果
    'blur',  # 模糊
    'texture',  # 紋理
    'highlights',  # 高光
    'shadows',  # 陰影
    'filter',  # 濾鏡
    'vintage effect',  # 復古效果
    'glow',  # 光暈
    'gradient effect',  # 漸變效果
    'distortion',  # 失真效果
    'refraction effect',  # 折射效果
    'noise',  # 雜訊
    'fog effect',  # 霧化
    'brightness adjustment',  # 亮度調整
    'reflection effect'  # 反射效果
]

composition = [  # 構圖
    'central composition',  # 中心構圖
    'diagonal composition',  # 對角構圖
    'golden ratio',  # 黃金分割構圖
    'rule of thirds',  # 三分法構圖
    'symmetrical composition',  # 對稱構圖
    'asymmetrical composition',  # 非對稱構圖
    'framed composition',  # 框架構圖
    'leading lines',  # 引導線構圖
    'minimal composition',  # 簡約構圖
    'complex composition'  # 複雜構圖
]

# Characters (人物類)
age = [  # 年齡
    'child',  # 幼年
    'teen',  # 少年
    'young adult',  # 青少年
    'adult',  # 青年
    'mature',  # 成熟
    'middle-aged',  # 中年
    'elderly',  # 老年
    'baby',  # 嬰兒
    'all ages',  # 老少皆宜
    ''
]

gender = [  # 性別
    'male',  # 男性
    'female',  # 女性
    'non-binary',  # 中性
    'androgynous',  # 雙性
    'unspecified',  # 不確定
    'transgender',  # 跨性別
    ''
]

人数 = [  # 人數
    'solo',  # 單人
    'group',  # 群體
    'duo',  # 雙人
    'trio',  # 三人
    'multiple people',  # 多人
    'team',  # 隊伍
    'crowd',  # 群眾
    ''
]

roles_and_jobs = [  # 角色與職業
    'hero',  # 英雄
    'villain',  # 反派
    'ninja',  # 忍者
    'mage',  # 法師
    'warrior',  # 戰士
    'doctor',  # 醫生
    'scientist',  # 科學家
    'knight',  # 騎士
    'spy',  # 間諜
    'hunter',  # 獵人
    'barbarian',  # 野蠻人
    'student',  # 學生
    'wanderer',  # 流浪者
    'prince',  # 王子
    'princess',  # 公主
    'artist',  # 畫家
    'musician',  # 音樂家
    'writer',  # 作家
    'police',  # 警察
    'firefighter',  # 消防員
    'teacher',  # 教師
    'engineer',  # 工程師
    'detective',  # 偵探
    'explorer',  # 探險家
    'chef',  # 廚師
    'pilot',  # 飛行員
    ''
]

skin_tone = [  # 膚色
    'fair',  # 白皙
    'dark',  # 深膚色
    'tan',  # 褐色
    'yellow',  # 黃種膚色
    'light',  # 淺膚色
    'pale',  # 青白色
    'bronze',  # 古銅色
    'black',  # 黝黑色
    'grey',  # 灰白色
    ''
]

body_type = [  # 體型
    'slim',  # 瘦弱
    'muscular',  # 健壯
    'curvy',  # 豐滿
    'petite',  # 嬌小
    'tall',  # 高大
    'short',  # 矮胖
    'medium build',  # 中等身材
    'giant',  # 巨人
    'pregnant',  # 懷孕
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
    '長度': ['短', '中', '長', '超短', '超長', ''],
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

# Appearance (外觀)
facial_features = {  # 五官
    'eyebrows': ['thick', 'thin', 'well-groomed', 'arched', 'bushy', 'delicate', ''],  # 眉毛
    'eye_color': ['blue', 'green', 'brown', 'black', 'grey', 'gold', 'purple', 'red', ''],  # 眼睛顏色
    'mouth': ['smile', 'grim', 'pout', 'wide smile', 'closed', 'open', ''],  # 嘴巴
    'ears': ['pointed', 'round', 'elf ears', 'animal ears', 'large ears', 'small ears', ''],  # 耳朵
    'beard': ['rough', 'well-trimmed', 'goatee', 'full beard', 'mustache', 'no beard', ''],  # 鬍子
    'teeth': ['straight', 'sharp', 'fangs', 'missing teeth', 'white teeth', '']  # 牙齒
}

hair = {  # 頭髮
    'length': ['short', 'medium', 'long', 'extra short', 'extra long', ''],  # 長度
    'color': ['black', 'gold', 'red', 'white', 'purple', 'blue', 'green', 'silver', 'brown', ''],  # 顏色
    'bangs': ['middle part', 'straight bangs', 'side bangs', 'no bangs', ''],  # 瀏海
    'braids': ['single braid', 'double braids', 'loose braids', 'no braids', ''],  # 辮子
    'style': ['curly', 'straight', 'wavy', 'ponytail', 'bun', ''],  # 髮型
}

upper_body = {  # 上半身
    'chest': ['flat', 'full', 'small', 'large', 'average', ''],  # 胸部
    'waist': ['slim', 'muscular', 'thick', 'petite', 'no waist', ''],  # 腰部
    'back': ['smooth', 'tattoos', 'scars', 'wings', '']  # 背部
}

lower_body = {  # 下半身
    'butt': ['round', 'flat', 'full', 'small', 'large', ''],  # 屁股
    'legs': ['long', 'muscular', 'slender', 'thick', 'short', ''],  # 腿部
    'feet': ['barefoot', 'wearing shoes', 'wearing boots', 'wearing sandals', '']  # 腳步
}

tail = ['fox tail', 'dragon tail', 'cat tail', 'dog tail', 'snake tail', 'no tail', '']  # 尾巴

wings = ['angel wings', 'demon wings', 'bat wings', 'bird wings', 'dragon wings', 'no wings', '']  # 翅膀

horns = ['single horn', 'double horns', 'antlers', 'ram horns', 'bull horns', 'no horns', '']  # 角

# Clothing (服裝)
full_body_clothing = [  # 全身服裝
    'armor',  # 戰甲
    'dress',  # 禮服
    'casual wear',  # 便服
    'sportswear',  # 運動服
    'kimono',  # 和服
    'school uniform',  # 校服
    'tuxedo',  # 燕尾服
    'cape',  # 披風
    'thief outfit',  # 盜賊裝
    'suit',  # 西裝
    'samurai armor',  # 武士服
    'gown',  # 晚禮服
    'naked, nude',  # 裸體
    ''
]

clothing_style = [  # 衣服風格
    'modern',  # 現代時尚
    'vintage',  # 古典復古
    'punk',  # 朋克風
    'street',  # 街頭風
    'gothic',  # 哥德風
    'casual',  # 休閒風
    'sports',  # 運動風
    'high-tech',  # 高科技未來風
    'fantasy',  # 奇幻風
    'ancient',  # 古風
    'military',  # 軍裝風
    'romantic',  # 浪漫風
    'medieval',  # 中世紀風
    ''
]

accessories = [  # 裝飾
    'embroidery',  # 刺繡
    'tassels',  # 流蘇
    'pearls',  # 珍珠
    'diamonds',  # 鑽石
    'metal chains',  # 金屬鏈
    'ribbons',  # 絲帶
    'badges',  # 徽章
    'crystals',  # 水晶
    'feathers',  # 裝飾羽毛
    'sequins',  # 亮片
    ''
]

# Head, upper, and lower body accessories
head_accessories = [  # 頭部配件
    'hat',  # 帽子
    'hair clip',  # 髪飾
    'mask',  # 面具
    'scarf',  # 頭巾
    'goggles',  # 護目鏡
    'helmet',  # 頭盔
    'glasses',  # 眼鏡
    'cat ears',  # 貓耳
    'rabbit ears',  # 兔耳
    'hairband',  # 髮帶
    'veil',  # 頭紗
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

upper_body_accessories = [  # 上半身配件
    'gloves',  # 手飾
    'necklace',  # 項鍊
    'bracelet',  # 手鐲
    'shoulder pads',  # 肩章
    'ring',  # 戒指
    'watch',  # 手錶
    ''
]

lower_body_accessories = [  # 下半身配件
    'boots',  # 靴子
    'high heels',  # 高跟鞋
    'socks',  # 襪子
    'kneepads',  # 護膝
    'ankle bracelets',  # 腳鐲
    'sandals',  # 涼鞋
    'sneakers',  # 運動鞋
    ''
]

# Poses (姿勢)
poses = {  # 動作
    'action': [
        'running',  # 跑步
        'standing',  # 站立
        'walking',  # 行走
        'jumping',  # 跳躍
        'squatting',  # 蹲下
        'kneeling',  # 跪姿
        'flying',  # 飛行姿勢
        'kicking',  # 踢腿
        'fighting stance',  # 格鬥姿勢
        'hugging',  # 擁抱
        'raising hand',  # 抬手
        'fist clenching',  # 握拳
        ''
    ],
    'gaze': [
        'straight ahead',  # 正視
        'sideways',  # 側視
        'upward',  # 仰視
        'downward',  # 俯視
        'looking back',  # 回頭
        'narrowed eyes',  # 瞇眼
        'staring',  # 凝視
        'glancing',  # 瞟視
        ''
    ],
    'expression': [
        'smiling',  # 微笑
        'angry',  # 憤怒
        'surprised',  # 驚訝
        'sad',  # 悲傷
        'happy',  # 開心
        'serious',  # 冷酷
        'shy',  # 害羞
        'anxious',  # 焦慮
        'confident',  # 自信
        ''
    ],
    'emotion': [
        'joyful',  # 愉悅
        'sad',  # 悲傷
        'calm',  # 平靜
        'excited',  # 激動
        'angry',  # 憤怒
        'nervous',  # 緊張
        'surprised',  # 驚喜
        'frustrated',  # 沮喪
        'satisfied',  # 滿足
        'jealous',  # 嫉妒
        'desperate',  # 絕望
        ''
    ],
    'upper_body': [
        'hands on hips',  # 雙手插腰
        'crossed arms',  # 交叉雙臂
        'raising hand',  # 抬手
        'holding weapon',  # 手持武器
        ''
    ],
    'lower_body': [
        'standing still',  # 靜止站姿
        'squatting',  # 蹲姿
        'crossed legs',  # 雙腿交叉
        ''
    ]
}

# Environment (環境類)
seasons = [  # 季節
    'spring',  # 春
    'summer',  # 夏
    'autumn',  # 秋
    'winter',  # 冬
    'rainy season',  # 雨季
    'dry season',  # 乾季
    'snow season',  # 雪季
    'typhoon season',  # 颱風季
    ''
]

atmosphere = [  # 氛圍
    'warm',  # 溫暖
    'gloomy',  # 陰森
    'romantic',  # 浪漫
    'mysterious',  # 神秘
    'relaxed',  # 輕鬆
    'tense',  # 緊張
    'fantastical',  # 奇幻
    'futuristic',  # 未來感
    'surreal',  # 超現實
    'classical',  # 古典
    ''
]

lighting = [  # 光線效果
    'backlit',  # 背光
    'side-lit',  # 側光
    'moonlight',  # 月光
    'candlelight',  # 燭光
    'starlight',  # 星光
    'sunlight',  # 陽光
    'dusk light',  # 黃昏光
    'morning light',  # 晨光
    'lightning',  # 閃電光
    ''
]

outdoor = [  # 室外
    'skyscrapers',  # 高樓大廈
    'countryside cottage',  # 鄉村小屋
    'forest',  # 森林
    'desert',  # 沙漠
    'beach',  # 海邊
    'mountains',  # 山脈
    'garden',  # 花園
    'castle',  # 城堡
    'waterfall',  # 瀑布
    ''
]

indoor = [  # 室內
    'living room',  # 客廳
    'kitchen',  # 廚房
    'bedroom',  # 臥室
    'office',  # 辦公室
    'library',  # 書房
    'bathroom',  # 浴室
    'studio',  # 工作室
    'hall',  # 大廳
    'church',  # 教堂
    ''
]