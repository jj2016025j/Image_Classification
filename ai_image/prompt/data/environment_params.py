# environment_params.py

# 室外背景參數
OUTDOOR_PARAMS = {
    'skyscrapers': {'positive': 0.8, 'negative': 0.2},
    'countryside cottage': {'positive': 0.7, 'negative': 0.3},
    'forest': {'positive': 0.9, 'negative': 0.1},
    'desert': {'positive': 0.6, 'negative': 0.4},
    'beach': {'positive': 0.8, 'negative': 0.2},
    'mountains': {'positive': 0.9, 'negative': 0.1},
    'garden': {'positive': 0.7, 'negative': 0.3},
    'castle': {'positive': 0.6, 'negative': 0.4},
    'waterfall': {'positive': 0.8, 'negative': 0.2}
}

# 室內背景參數
INDOOR_PARAMS = {
    'living room': {'positive': 0.9, 'negative': 0.1},
    'kitchen': {'positive': 0.8, 'negative': 0.2},
    'bedroom': {'positive': 0.9, 'negative': 0.1},
    'office': {'positive': 0.7, 'negative': 0.3},
    'library': {'positive': 0.8, 'negative': 0.2},
    'bathroom': {'positive': 0.6, 'negative': 0.4},
    'studio': {'positive': 0.7, 'negative': 0.3},
    'hall': {'positive': 0.6, 'negative': 0.4},
    'church': {'positive': 0.5, 'negative': 0.5}
}

# 季節參數
SEASON_PARAMS = {
    'spring': {'positive': 0.8, 'negative': 0.2},
    'summer': {'positive': 0.9, 'negative': 0.1},
    'autumn': {'positive': 0.7, 'negative': 0.3},
    'winter': {'positive': 0.9, 'negative': 0.1},
    'rainy season': {'positive': 0.5, 'negative': 0.5},
    'dry season': {'positive': 0.4, 'negative': 0.6},
    'snow season': {'positive': 0.6, 'negative': 0.4},
    'typhoon season': {'positive': 0.3, 'negative': 0.7}
}

# 氣氛參數
ATMOSPHERE_PARAMS = {
    'warm': {'positive': 0.9, 'negative': 0.1},
    'gloomy': {'positive': 0.6, 'negative': 0.4},
    'romantic': {'positive': 0.8, 'negative': 0.2},
    'mysterious': {'positive': 0.7, 'negative': 0.3},
    'relaxed': {'positive': 0.9, 'negative': 0.1},
    'tense': {'positive': 0.5, 'negative': 0.5},
    'fantastical': {'positive': 0.6, 'negative': 0.4},
    'futuristic': {'positive': 0.4, 'negative': 0.6},
    'surreal': {'positive': 0.5, 'negative': 0.5},
    'classical': {'positive': 0.8, 'negative': 0.2}
}
