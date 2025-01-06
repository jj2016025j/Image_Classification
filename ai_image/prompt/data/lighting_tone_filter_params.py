# lighting_tone_filter_params.py

# 光影提示詞與權重
LIGHTING_PROMPTS = {
    'Bright': {'positive': 1, 'negative': 0.1},
    'Soft': {'positive': 0.8, 'negative': 0.2},
    'Backlight': {'positive': 0.7, 'negative': 0.3},
    'backlit': {'positive': 0.7, 'negative': 0.3},
    'side-lit': {'positive': 0.7, 'negative': 0.3},
    'moonlight': {'positive': 0.7, 'negative': 0.3},
    'candlelight': {'positive': 0.7, 'negative': 0.3},
    'starlight': {'positive': 0.7, 'negative': 0.3},
    'sunlight': {'positive': 0.7, 'negative': 0.3},
    'dusk light': {'positive': 0.7, 'negative': 0.3},
    'morning light': {'positive': 0.7, 'negative': 0.3},
    'lightning': {'positive': 0.7, 'negative': 0.3},
}

# 色調提示詞與權重
TONE_PROMPTS = {
    'Cool': {'positive': 1, 'negative': 0.1},
    'Warm': {'positive': 0.8, 'negative': 0.2},
    'Monochrome': {'positive': 0.7, 'negative': 0.3},
}

# 濾鏡提示詞與權重
FILTER_PROMPTS = {
    'Vintage': {'positive': 1, 'negative': 0.1},
    'HDR': {'positive': 0.9, 'negative': 0.2},
    'Black and White': {'positive': 0.8, 'negative': 0.3},
}
