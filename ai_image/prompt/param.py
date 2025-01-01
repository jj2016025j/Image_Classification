 
from ai_image.config import ParamsConfig
from ai_image.prompt.negative_generator import get_negatives
from ai_image.prompt.parameter_generator import generate_parameters
from ai_image.prompt.model import get_random_model


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
    取得預設參數，生成隨機提示詞，選擇隨機模型、採樣器(Upscaler、Sampling method)
    """
    adjust_params = ParamsConfig().to_dict()
    print(f"API預設參數: {adjust_params}")
    
    parameters_string = generate_parameters(mode='positive')
    print(f"正面提示詞: {parameters_string}")
    adjust_params["prompt"] = parameters_string
    
    negatives_string = generate_parameters(mode='negative')
    print(f"負面提示詞: {negatives_string}")
    adjust_params["negative_prompt"] = negatives_string
    
    model_name = get_random_model()
    adjust_params["override_settings"]["sd_model_checkpoint"] = model_name


    return adjust_params