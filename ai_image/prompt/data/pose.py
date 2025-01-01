class Poses:
    """姿勢相關屬性與權重"""

    # 動作屬性
    action = {
        'running': {'positive': 0.8, 'negative': 0.2},         # 跑步
        'standing': {'positive': 0.6, 'negative': 0.4},       # 站立
        'walking': {'positive': 0.7, 'negative': 0.3},        # 行走
        'jumping': {'positive': 0.5, 'negative': 0.5},        # 跳躍
        'squatting': {'positive': 0.4, 'negative': 0.6},      # 蹲下
        'kneeling': {'positive': 0.3, 'negative': 0.7},       # 跪姿
        'flying': {'positive': 0.2, 'negative': 0.8},         # 飛行姿勢
        'kicking': {'positive': 0.3, 'negative': 0.7},        # 踢腿
        'fighting stance': {'positive': 0.4, 'negative': 0.6},# 格鬥姿勢
        'hugging': {'positive': 0.3, 'negative': 0.7},        # 擁抱
        'raising hand': {'positive': 0.5, 'negative': 0.5},   # 抬手
        'fist clenching': {'positive': 0.2, 'negative': 0.8}, # 握拳
        None: {'positive': 0.1, 'negative': 0.9}             # 無動作
    }

    # 視線屬性
    gaze = {
        'straight ahead': {'positive': 0.7, 'negative': 0.3}, # 正視
        'sideways': {'positive': 0.6, 'negative': 0.4},       # 側視
        'upward': {'positive': 0.5, 'negative': 0.5},         # 仰視
        'downward': {'positive': 0.4, 'negative': 0.6},       # 俯視
        'looking back': {'positive': 0.3, 'negative': 0.7},   # 回頭
        'narrowed eyes': {'positive': 0.2, 'negative': 0.8},  # 瞇眼
        'staring': {'positive': 0.6, 'negative': 0.4},        # 凝視
        'glancing': {'positive': 0.3, 'negative': 0.7},       # 瞟視
        None: {'positive': 0.1, 'negative': 0.9}             # 無視線
    }

    # 表情屬性
    expression = {
        'smiling': {'positive': 0.7, 'negative': 0.3},        # 微笑
        'angry': {'positive': 0.5, 'negative': 0.5},          # 憤怒
        'surprised': {'positive': 0.6, 'negative': 0.4},      # 驚訝
        'sad': {'positive': 0.4, 'negative': 0.6},            # 悲傷
        'happy': {'positive': 0.8, 'negative': 0.2},          # 開心
        'serious': {'positive': 0.5, 'negative': 0.5},        # 冷酷
        'shy': {'positive': 0.3, 'negative': 0.7},            # 害羞
        'anxious': {'positive': 0.2, 'negative': 0.8},        # 焦慮
        'confident': {'positive': 0.6, 'negative': 0.4},      # 自信
        None: {'positive': 0.1, 'negative': 0.9}             # 無表情
    }

    # 情感屬性
    emotion = {
        'joyful': {'positive': 0.8, 'negative': 0.2},         # 愉悅
        'sad': {'positive': 0.4, 'negative': 0.6},            # 悲傷
        'calm': {'positive': 0.6, 'negative': 0.4},           # 平靜
        'excited': {'positive': 0.7, 'negative': 0.3},        # 激動
        'angry': {'positive': 0.5, 'negative': 0.5},          # 憤怒
        'nervous': {'positive': 0.3, 'negative': 0.7},        # 緊張
        'surprised': {'positive': 0.6, 'negative': 0.4},      # 驚喜
        'frustrated': {'positive': 0.2, 'negative': 0.8},     # 沮喪
        'satisfied': {'positive': 0.7, 'negative': 0.3},      # 滿足
        'jealous': {'positive': 0.3, 'negative': 0.7},        # 嫉妒
        'desperate': {'positive': 0.2, 'negative': 0.8},      # 絕望
        None: {'positive': 0.1, 'negative': 0.9}             # 無情感
    }

    # 手部動作屬性
    arm_action = {
        'hands on hips': {'positive': 0.7, 'negative': 0.3},  # 雙手插腰
        'crossed arms': {'positive': 0.6, 'negative': 0.4},   # 交叉雙臂
        'raising hand': {'positive': 0.5, 'negative': 0.5},   # 抬手
        'holding weapon': {'positive': 0.3, 'negative': 0.7}, # 手持武器
        None: {'positive': 0.1, 'negative': 0.9}             # 無動作
    }

    # 腿部動作屬性
    leg_action = {
        'standing still': {'positive': 0.7, 'negative': 0.3}, # 靜止站姿
        'squatting': {'positive': 0.4, 'negative': 0.6},      # 蹲姿
        'crossed legs': {'positive': 0.5, 'negative': 0.5},   # 雙腿交叉
        None: {'positive': 0.1, 'negative': 0.9}             # 無動作
    }
