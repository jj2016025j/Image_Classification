# style_params.py

# 寫實風格參數
REALISTIC_PROMPTS = {
    'photo realistic': {'positive': 1, 'negative': 0.1},
    'CG': {'positive': 0.8, 'negative': 0.2},
    '3D rendering style': {'positive': 0.7, 'negative': 0.3},
    'artbook': {'positive': 0.6, 'negative': 0.4}
}

# 藝術風格參數
ARTISTIC_PROMPTS = {
    'hand-drawn style': {'positive': 1, 'negative': 0.1},
    'illustration': {'positive': 0.9, 'negative': 0.2},
    'fantasy': {'positive': 0.8, 'negative': 0.3},
    'art nouveau': {'positive': 0.7, 'negative': 0.4},
    'watercolor style': {'positive': 0.6, 'negative': 0.5},
    'oil painting style': {'positive': 0.7, 'negative': 0.4},
    'sketch style': {'positive': 0.5, 'negative': 0.6}
}

# 動畫風格參數
ANIME_PROMPTS = {
    'anime': {'positive': 1, 'negative': 0.1},
    'anime coloring': {'positive': 0.9, 'negative': 0.2},
    '2D': {'positive': 0.8, 'negative': 0.3},
    'comic style': {'positive': 0.7, 'negative': 0.4},
    'pixel art': {'positive': 0.6, 'negative': 0.5}
}

# 歷史風格參數
HISTORICAL_PROMPTS = {
    'impressionism': {'positive': 1, 'negative': 0.1},
    'baroque': {'positive': 0.8, 'negative': 0.3},
    'retro style': {'positive': 0.7, 'negative': 0.4}
}
