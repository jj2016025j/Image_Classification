import json
import re
from typing import Dict

class ImageParser:
    """ 圖片資訊解析類別 """

    @staticmethod
    def parse_image_parameters(info: str) -> Dict[str, str]:
        """解析圖片 metadata"""
        parameters_dict = {}
        try:
            parameters_dict = json.loads(info)
        except json.JSONDecodeError:
            print("圖片資訊格式錯誤，無法解析")
        return parameters_dict

    @staticmethod
    def get_model_name_from_image_info(info: Dict[str, str]) -> str:
        """從 metadata 提取 Model 名稱"""
        return info.get('Model', 'No model name found')
