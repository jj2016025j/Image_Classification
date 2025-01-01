class Clothing:
    """服裝屬性與權重"""

    # 全身服裝屬性
    full_body = {
        'armor': {'positive': 5, 'negative': 0},  # 戰甲
        'dress': {'positive': 10, 'negative': 0},  # 禮服
        'casual wear': {'positive': 20, 'negative': 0},  # 便服
        'sportswear': {'positive': 15, 'negative': 0},  # 運動服
        'kimono': {'positive': 10, 'negative': 0},  # 和服
        'school uniform': {'positive': 10, 'negative': 0},  # 校服
        'tuxedo': {'positive': 5, 'negative': 0},  # 燕尾服
        'cape': {'positive': 3, 'negative': 0},  # 披風
        'thief outfit': {'positive': 4, 'negative': 0},  # 盜賊裝
        'suit': {'positive': 8, 'negative': 0},  # 西裝
        'samurai armor': {'positive': 2, 'negative': 0},  # 武士服
        'gown': {'positive': 7, 'negative': 0},  # 晚禮服
        'naked, nude': {'positive': 1, 'negative': 0},  # 裸體
        None: {'positive': 30, 'negative': 0}  # 無
    }

    # 服裝風格屬性
    style = {
        'modern': {'positive': 20, 'negative': 0},  # 現代時尚
        'vintage': {'positive': 10, 'negative': 0},  # 古典復古
        'punk': {'positive': 5, 'negative': 0},  # 朋克風
        'street': {'positive': 15, 'negative': 0},  # 街頭風
        'gothic': {'positive': 8, 'negative': 0},  # 哥德風
        'casual': {'positive': 25, 'negative': 0},  # 休閒風
        'sports': {'positive': 10, 'negative': 0},  # 運動風
        'high-tech': {'positive': 5, 'negative': 0},  # 高科技未來風
        'fantasy': {'positive': 10, 'negative': 0},  # 奇幻風
        'ancient': {'positive': 7, 'negative': 0},  # 古風
        'military': {'positive': 4, 'negative': 0},  # 軍裝風
        'romantic': {'positive': 6, 'negative': 0},  # 浪漫風
        'medieval': {'positive': 3, 'negative': 0},  # 中世紀風
        None: {'positive': 30, 'negative': 0}  # 無
    }

    # 配件屬性
    accessories = {
        'embroidery': {'positive': 10, 'negative': 0},  # 刺繡
        'tassels': {'positive': 8, 'negative': 0},  # 流蘇
        'pearls': {'positive': 7, 'negative': 0},  # 珍珠
        'diamonds': {'positive': 5, 'negative': 0},  # 鑽石
        'metal chains': {'positive': 4, 'negative': 0},  # 金屬鏈
        'ribbons': {'positive': 10, 'negative': 0},  # 絲帶
        'badges': {'positive': 3, 'negative': 0},  # 徽章
        'crystals': {'positive': 6, 'negative': 0},  # 水晶
        'feathers': {'positive': 5, 'negative': 0},  # 裝飾羽毛
        'sequins': {'positive': 2, 'negative': 0},  # 亮片
        None: {'positive': 40, 'negative': 0}  # 無
    }

class Accessories:
    """配件屬性與權重"""

    # 頭部配件屬性
    head = {
        'hat': {'positive': 15, 'negative': 0},  # 帽子
        'hair clip': {'positive': 10, 'negative': 0},  # 髮飾
        'mask': {'positive': 8, 'negative': 0},  # 面具
        'scarf': {'positive': 6, 'negative': 0},  # 頭巾
        'goggles': {'positive': 5, 'negative': 0},  # 護目鏡
        'helmet': {'positive': 4, 'negative': 0},  # 頭盔
        'glasses': {'positive': 20, 'negative': 0},  # 眼鏡
        'cat ears': {'positive': 7, 'negative': 0},  # 貓耳
        'rabbit ears': {'positive': 6, 'negative': 0},  # 兔耳
        'hairband': {'positive': 10, 'negative': 0},  # 髮帶
        'veil': {'positive': 5, 'negative': 0},  # 頭紗
        None: {'positive': 30, 'negative': 0}  # 無
    }

    # 上半身配件屬性
    upper_body = {
        'gloves': {'positive': 10, 'negative': 0},  # 手套
        'necklace': {'positive': 15, 'negative': 0},  # 項鍊
        'bracelet': {'positive': 12, 'negative': 0},  # 手鐲
        'shoulder pads': {'positive': 5, 'negative': 0},  # 肩章
        'ring': {'positive': 10, 'negative': 0},  # 戒指
        'watch': {'positive': 8, 'negative': 0},  # 手錶
        None: {'positive': 40, 'negative': 0}  # 無
    }

    # 下半身配件屬性
    lower_body = {
        'boots': {'positive': 15, 'negative': 0},  # 靴子
        'high heels': {'positive': 10, 'negative': 0},  # 高跟鞋
        'socks': {'positive': 20, 'negative': 0},  # 襪子
        'kneepads': {'positive': 5, 'negative': 0},  # 護膝
        'ankle bracelets': {'positive': 7, 'negative': 0},  # 腳鐲
        'sandals': {'positive': 10, 'negative': 0},  # 涼鞋
        'sneakers': {'positive': 15, 'negative': 0},  # 運動鞋
        None: {'positive': 30, 'negative': 0}  # 無
    }
