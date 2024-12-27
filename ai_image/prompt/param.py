 
from ai_image.config import ParamsConfig
from ai_image.prompt.negative_generator import get_negatives
from ai_image.prompt.parameter_generator import get_parameters
from ai_image.prompt.model import get_model


def custom_params(custom_params=None):
    """
    調整參數
    """
    default_params = ParamsConfig().to_dict()

    # 如果提供了自定義參數，更新相應的值
    if custom_params:
        default_params.update(custom_params)
    print(f"修改後參數內容: {default_params}")

    return default_params
        
def adjust_params():
    """
    隨機參數
    """
    default_params = ParamsConfig().to_dict()
    
    parameters_string = get_parameters()
    default_params["prompt"] = parameters_string
    
    negatives_string = get_negatives()
    default_params["negative_prompt"] = negatives_string
    
    model_name = get_model()
    default_params["override_settings"]["sd_model_checkpoint"] = model_name

    print(f"參數內容: {default_params}")

    return default_params