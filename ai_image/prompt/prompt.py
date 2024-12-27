import random
from ai_image.sd_api import fetch_models
from ai_image.config import ParamsConfig
from ai_image.prompt.negative_generator import get_negatives
from ai_image.prompt.parameter_generator import get_parameters
    
def get_model_name():
    """
    取得模型名稱
    """
    model = {
        "model_name":"best_meinaunreal_v1Beta"
    }
    
    return model
    
def get_random_model():
    """
    隨機選擇模型
    """
    # 獲取可用模型列表
    models = fetch_models()
    filtered_models = [model for model in models if "best" in model["model_name"]]
    
    # 檢查是否有符合條件的模型
    if not filtered_models:
        raise Exception("No models found with '較優' in model_name")
    
    # 從篩選後的模型中隨機選擇一個
    selected_model = random.choice(filtered_models)
    return selected_model
    
        
def adjust_params(custom_params=None):
    """
    調整參數
    """
    default_params = ParamsConfig().to_dict()
    
    parameters_string = get_parameters()
    negatives_string = get_negatives()
    selected_model = get_model_name()
    model_name = selected_model["model_name"]

    default_params["prompt"] = parameters_string
    default_params["negative_prompt"] = negatives_string
    default_params["override_settings"]["sd_model_checkpoint"] = model_name

    # 如果提供了自定義參數，更新相應的值
    if custom_params:
        default_params.update(custom_params)

    return default_params