numbers = {
    'solo': 0.9,  # 單人
    'group': 0.08,  # 群體
    'duo': 0.01,  # 雙人
    'trio': 0.007,  # 三人
    'multiple people': 0.003,  # 多人
    'team': 0.001  # 隊伍
}

gender = {
    'male': 0.2,
    'female': 0.9,
    'non-binary': 0.3,
    'androgynous': 0.2,
    'unspecified': 0.1,
    'transgender': 0.2,
}

# 年齡
age = {
    'child': 0.3,
    'teen': 0.5,
    'young adult': 0.8,
    'adult': 0.7,
    'mature': 0.6,
    'middle-aged': 0.4,
    'elderly': 0.3,
    'baby': 0.2,
    'all ages': 0.1,
}

# 膚色
skin_tone = {
    'fair': 0.8,
    'dark': 0.7,
    'tan': 0.6,
    'yellow': 0.7,
    'light': 0.6,
    'pale': 0.5,
    'bronze': 0.4,
    'black': 0.3,
    'grey': 0.2
}

# 體型
body_type = {
    'slim': 0.8,
    'muscular': 0.7,
    'curvy': 0.6,
    'petite': 0.5,
    'tall': 0.7,
    'short': 0.5,
    'medium build': 0.6,
    'giant': 0.4,
    'pregnant': 0.2
}

# 五官
facial_features = {
    'eyebrows': {'thick': 0.8, 'thin': 0.7, 'well-groomed': 0.6, 'arched': 0.5, 'bushy': 0.4, 'delicate': 0.3},
    'eye_color': {'blue': 0.8, 'green': 0.7, 'brown': 0.6, 'black': 0.5, 'grey': 0.4, 'gold': 0.3, 'purple': 0.2, 'red': 0.1},
    'mouth': {'smile': 0.7, 'grim': 0.6, 'pout': 0.5, 'wide smile': 0.4, 'closed': 0.3, 'open': 0.2},
    'ears': {'pointed': 0.5, 'round': 0.5, 'elf ears': 0.4, 'animal ears': 0.3, 'large ears': 0.2, 'small ears': 0.1},
    'beard': {'rough': 0.4, 'well-trimmed': 0.3, 'goatee': 0.2, 'full beard': 0.3, 'mustache': 0.2, 'no beard': 0.6},
    'teeth': {'straight': 0.6, 'sharp': 0.5, 'fangs': 0.4, 'missing teeth': 0.3, 'white teeth': 0.7}
}

# 頭髮
hair = {
    'length': {'short': 0.5, 'medium': 0.6, 'long': 0.7, 'extra short': 0.4, 'extra long': 0.3},
    'color': {'black': 0.7, 'gold': 0.6, 'red': 0.5, 'white': 0.4, 'purple': 0.3, 'blue': 0.2, 'green': 0.1, 'silver': 0.2, 'brown': 0.6},
    'bangs': {'middle part': 0.5, 'straight bangs': 0.4, 'side bangs': 0.3, 'no bangs': 0.6},
    'braids': {'single braid': 0.4, 'double braids': 0.3, 'loose braids': 0.5, 'no braids': 0.7},
    'style': {'curly': 0.5, 'straight': 0.6, 'wavy': 0.7, 'ponytail': 0.4, 'bun': 0.3}
}

# 身體細節
body_details = {
    'chest': {'flat': 0.5, 'full': 0.6, 'small': 0.5, 'large': 0.4, 'average': 0.7},
    'waist': {'slim': 0.6, 'muscular': 0.5, 'thick': 0.4, 'petite': 0.3, 'no waist': 0.2},
    'back': {'smooth': 0.5, 'tattoos': 0.4, 'scars': 0.3, 'wings': 0.2},
    'butt': {'round': 0.6, 'flat': 0.5, 'full': 0.4, 'small': 0.3, 'large': 0.2},
    'legs': {'long': 0.5, 'muscular': 0.4, 'slender': 0.6, 'thick': 0.3, 'short': 0.2},
    'feet': {'barefoot': 0.4, 'wearing shoes': 0.5, 'wearing boots': 0.6, 'wearing sandals': 0.3}
}

# 尾巴、翅膀、角
tail = {
    'fox tail': 0.6, 'dragon tail': 0.5, 'cat tail': 0.4, 'dog tail': 0.3, 'snake tail': 0.2, 'no tail': 0.7
}
wings = {
    'angel wings': 0.6, 'demon wings': 0.5, 'bat wings': 0.4, 'bird wings': 0.3, 'dragon wings': 0.2, 'no wings': 0.7
}
horns = {
    'single horn': 0.4, 'double horns': 0.5, 'antlers': 0.6, 'ram horns': 0.3, 'bull horns': 0.2, 'no horns': 0.7
}
