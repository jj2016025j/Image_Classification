# image_quality_params.py

# 圖像品質的權重配置
IMAGE_QUALITY_OPTIONS = {
    'masterpiece': {'positive': 1, 'negative': 0},
    'best quality': {'positive': 1, 'negative': 0},
    'amazing quality': {'positive': 0.5, 'negative': 0},
    'high quality': {'positive': 0.5, 'negative': 0},
    'ultra high res': {'positive': 0.5, 'negative': 0},
    '4K': {'positive': 0.2, 'negative': 0},
    '8K': {'positive': 0.5, 'negative': 0},
    '4K quality': {'positive': 0.2, 'negative': 0},
    '8K quality': {'positive': 0.5, 'negative': 0},
    'high resolution': {'positive': 0.2, 'negative': 0},
    
    'super high resolution': {'positive': 0.2, 'negative': 0},
    'highres': {'positive': 0.2, 'negative': 0},
    'HDR': {'positive': 0.2, 'negative': 0},
    'HD': {'positive': 0.2, 'negative': 0},
    'delicate quality': {'positive': 0.2, 'negative': 0},
    'enhanced dynamic range': {'positive': 0.2, 'negative': 0},
    'ray tracing effect': {'positive': 0.2, 'negative': 0},
    'ultra-detailed': {'positive': 0.2, 'negative': 0},
    'very detailed': {'positive': 0.2, 'negative': 0},
    'score_9': {'positive': 1, 'negative': 0},
    
    'score_8_up': {'positive': 1, 'negative': 0},
    'score_8': {'positive': 1, 'negative': 0},
    'score_7_up': {'positive': 0.2, 'negative': 0},
    'score_6_up': {'positive': 0.2, 'negative': 0},
    'score_5_up': {'positive': 0.2, 'negative': 0},
    'score_4_up': {'positive': 0.2, 'negative': 0},
    
    'score_6': {'positive': 0, 'negative': 1},
    'score_5': {'positive': 0, 'negative': 1},
    'score_4': {'positive': 0, 'negative': 1},
    'score_3': {'positive': 0, 'negative': 1},
    'score_2': {'positive': 0, 'negative': 1},
    'score_1': {'positive': 0, 'negative': 1},
    'worst quality': {'positive': 0, 'negative': 1},
    'bad quality': {'positive': 0, 'negative': 1},
    'low quality': {'positive': 0, 'negative': 1},
    'low res': {'positive': 0, 'negative': 1},
}

# 解析度的權重配置
RESOLUTION_OPTIONS = {
    'high resolution': {'positive': 1, 'negative': 0},
    'super high resolution': {'positive': 1, 'negative': 0},
    'highres': {'positive': 1, 'negative': 0},
    'HDR': {'positive': 1, 'negative': 0},
    '1080p': {'positive': 1, 'negative': 0},
    '4K': {'positive': 1, 'negative': 0},
    '8K': {'positive': 1, 'negative': 0},
    'Custom': {'positive': 0.8, 'negative': 0}
}

# 局部優化的權重配置
LOCAL_ENHANCEMENTS_OPTIONS = {
    'detailed highlights': {'positive': 1, 'negative': 0},
    'soft focus edges': {'positive': 0.9, 'negative': 0},
    'ultra-fine details': {'positive': 0.8, 'negative': 0},
    'lighting effects': {'positive': 1, 'negative': 0},
    'edge enhancement': {'positive': 0.7, 'negative': 0},
    'color correction': {'positive': 1, 'negative': 0},
    'contrast enhancement': {'positive': 1, 'negative': 0},
    'delicate texture': {'positive': 1, 'negative': 0},
    'shadow enhancement': {'positive': 0.9, 'negative': 0}
}
