import random
from prompt.API import fetch_models
from prompt.config import DEFAULT_PARAMS
from prompt.negative_generator import get_negatives
from prompt.parameter_generator import get_parameters
    
def adjust_params(custom_params=None):
    # 從預設參數開始
    params = DEFAULT_PARAMS.copy()
    
    # 獲取可用模型列表
    models = fetch_models()
    model = random.choice(models)
    model_name = model["model_name"]
    print('model:' + model["model_name"] + '\n')
   
    parameters_string = get_parameters()

    negatives_string = get_negatives()

    # 更新基本參數
    params["prompt"] = parameters_string
    params["negative_prompt"] = negatives_string
    params["override_settings"]["sd_model_checkpoint"] = model_name

    # 如果提供了自定義參數，更新相應的值
    if custom_params:
        params.update(custom_params)

    return params