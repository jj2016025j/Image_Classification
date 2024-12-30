# ai_image\prompt\data\imgae_quality.py

import random

class WeightedOptions:
    def __init__(self, options):
        """
        初始化權重選項
        :param options: 格式為 {key: {'positive': weight, 'negative': weight}}
        """
        self.options = options

    def generate_list(self, mode='positive', count=20):
        """
        根據指定模式生成列表，每個參數的權重獨立計算，權重為 1 的必選。
        :param mode: 'positive' 或 'negative'
        :param count: 返回的參數數量
        :return: 隨機選擇的參數列表
        """
        if mode not in ['positive', 'negative']:
            raise ValueError("Mode must be 'positive' or 'negative'")

        # 按模式提取有效選項
        weighted_choices = [(key, weights[mode]) for key, weights in self.options.items() if weights[mode] > 0]

        # 將權重為 1 的設為必選項
        mandatory = [key for key, weight in weighted_choices if weight == 1]

        # 從權重 <1 的選項中進行隨機選擇
        optional = [(key, weight) for key, weight in weighted_choices if 0 < weight < 1]
        optional_choices = []
        if optional:
            optional_keys = [key for key, _ in optional]
            optional_weights = [weight for _, weight in optional]
            # 按權重隨機選擇
            optional_choices = random.choices(
                population=optional_keys,
                weights=optional_weights,
                k=max(0, count - len(mandatory))
            )

        # 合併結果並限制數量
        selected = mandatory + optional_choices
        return selected[:count]


class ImageSettings:
    def __init__(self):
        # 圖像品質的權重配置
        self.image_quality = WeightedOptions({
            'masterpiece': {'positive': 1, 'negative': 0},  # 大師級作品
            'best quality': {'positive': 1, 'negative': 0},  # 最佳畫質
            'ultra high res': {'positive': 1, 'negative': 0},  # 超高解析度
            '4K': {'positive': 1, 'negative': 0},  # 4K畫質
            '8K': {'positive': 1, 'negative': 0},  # 8K畫質
            '4K quality': {'positive': 0.7, 'negative': 0},  # 4K質量
            '8K quality': {'positive': 0.7, 'negative': 0},  # 8K質量
            'high resolution': {'positive': 1, 'negative': 0},  # 高解析度
            'super high resolution': {'positive': 1, 'negative': 0},  # 超高解析度
            'highres': {'positive': 1, 'negative': 0},  # 高分辨率
            'HDR': {'positive': 1, 'negative': 0},  # 高動態範圍
            'delicate quality': {'positive': 1, 'negative': 0},  # 精緻質量
            'enhanced dynamic range': {'positive': 1, 'negative': 0},  # 增強動態範圍
            'ray tracing effect': {'positive': 1, 'negative': 0},  # 光線追蹤效果
            'ultra-detailed': {'positive': 1, 'negative': 0},  # 超詳細
            'score_9': {'positive': 1, 'negative': 0},  # 分數9
            'score_8_up': {'positive': 1, 'negative': 0},  # 分數8及以上
            'score_7_up': {'positive': 1, 'negative': 0},  # 分數7及以上
        })

        # 解析度的權重配置
        self.resolution = WeightedOptions({
            'high resolution': {'positive': 1, 'negative': 0},  # 高解析度
            'super high resolution': {'positive': 1, 'negative': 0},  # 超高解析度
            'highres': {'positive': 1, 'negative': 0},  # 高分辨率
            'HDR': {'positive': 1, 'negative': 0},  # 高動態範圍
            '1080p': {'positive': 1, 'negative': 0},  # 1080p解析度
            '4K': {'positive': 1, 'negative': 0},  # 4K解析度
            '8K': {'positive': 1, 'negative': 0},  # 8K解析度
            'Custom': {'positive': 0.8, 'negative': 0},  # 自定義解析度
        })

        # 局部優化的權重配置
        self.local_enhancements = WeightedOptions({
            'detailed highlights': {'positive': 1, 'negative': 0},  # 細節高光
            'soft focus edges': {'positive': 0.9, 'negative': 0},  # 柔焦邊緣
            'ultra-fine details': {'positive': 0.8, 'negative': 0},  # 超精細細節
            'lighting effects': {'positive': 1, 'negative': 0},  # 光影效果
            'edge enhancement': {'positive': 0.7, 'negative': 0},  # 邊緣增強
            'color correction': {'positive': 1, 'negative': 0},  # 色彩校正
            'contrast enhancement': {'positive': 1, 'negative': 0},  # 對比度增強
            'delicate texture': {'positive': 1, 'negative': 0},  # 細膩質感
            'shadow enhancement': {'positive': 0.9, 'negative': 0},  # 陰影增強
        })

    def generate_combined_list(self, mode='positive', count=30):
        """
        根據指定模式，結合不同配置生成綜合提示詞列表
        :param mode: 'positive' 或 'negative'
        :param count: 總提示詞數量
        :return: 合併的提示詞列表
        """
        quality_count = count // 2  # 平均分配給 image_quality
        enhancements_count = count - quality_count  # 剩餘分配給 local_enhancements

        quality_list = self.image_quality.generate_list(mode=mode, count=quality_count)
        resolution = self.resolution.generate_list(mode=mode, count=quality_count)
        enhancements_list = self.local_enhancements.generate_list(mode=mode, count=enhancements_count)

        return quality_list + resolution + enhancements_list


# 測試
if __name__ == "__main__":
    settings = ImageSettings()

    print("正面提示詞:")
    positive_list = settings.generate_combined_list(mode='positive', count=20)
    print(positive_list)

    print("負面提示詞:")
    negative_list = settings.generate_combined_list(mode='negative', count=20)
    print(negative_list)
