# Poses (姿勢)
action= {
    'running': 0.8,         # 跑步
    'standing': 0.6,       # 站立
    'walking': 0.7,        # 行走
    'jumping': 0.5,        # 跳躍
    'squatting': 0.4,      # 蹲下
    'kneeling': 0.3,       # 跪姿
    'flying': 0.2,         # 飛行姿勢
    'kicking': 0.3,        # 踢腿
    'fighting stance': 0.4,# 格鬥姿勢
    'hugging': 0.3,        # 擁抱
    'raising hand': 0.5,   # 抬手
    'fist clenching': 0.2, # 握拳
    None: 0.1              # 無動作
}
gaze= {
    'straight ahead': 0.7, # 正視
    'sideways': 0.6,       # 側視
    'upward': 0.5,         # 仰視
    'downward': 0.4,       # 俯視
    'looking back': 0.3,   # 回頭
    'narrowed eyes': 0.2,  # 瞇眼
    'staring': 0.6,        # 凝視
    'glancing': 0.3,       # 瞟視
    None: 0.1              # 無視線
}
expression= {
    'smiling': 0.7,        # 微笑
    'angry': 0.5,          # 憤怒
    'surprised': 0.6,      # 驚訝
    'sad': 0.4,            # 悲傷
    'happy': 0.8,          # 開心
    'serious': 0.5,        # 冷酷
    'shy': 0.3,            # 害羞
    'anxious': 0.2,        # 焦慮
    'confident': 0.6,      # 自信
    None: 0.1              # 無表情
}
emotion={
    'joyful': 0.8,         # 愉悅
    'sad': 0.4,           # 悲傷
    'calm': 0.6,          # 平靜
    'excited': 0.7,       # 激動
    'angry': 0.5,          # 憤怒
    'nervous': 0.3,        # 緊張
    'surprised': 0.6,      # 驚喜
    'frustrated': 0.2,     # 沮喪
    'satisfied': 0.7,      # 滿足
    'jealous': 0.3,        # 嫉妒
    'desperate': 0.2,      # 絕望
    None: 0.1              # 無情感
}
arm_action= {
    'hands on hips': 0.7,  # 雙手插腰
    'crossed arms': 0.6,   # 交叉雙臂
    'raising hand': 0.5,   # 抬手
    'holding weapon': 0.3, # 手持武器
    None: 0.1              # 無動作
}
leg_action= {
    'standing still': 0.7, # 靜止站姿
    'squatting': 0.4,      # 蹲姿
    'crossed legs': 0.5,   # 雙腿交叉
    None: 0.1              # 無動作
}
