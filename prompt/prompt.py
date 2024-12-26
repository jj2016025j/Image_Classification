import random
from prompt.SD_API import fetch_models
from prompt.config import DEFAULT_PARAMS, MODELS_NAME
from prompt.negative_generator import get_negatives
from prompt.parameter_generator import get_parameters
    
def adjust_params(custom_params=None):
    # 從預設參數開始
    params = DEFAULT_PARAMS.copy()
    
    # 獲取可用模型列表
    models = fetch_models()
    # 過濾 model_name 中包含 "較優" 的模型
    filtered_models = [model for model in models if MODELS_NAME in model["model_name"]]
    
    # 檢查是否有符合條件的模型
    if not filtered_models:
        raise Exception("No models found with '較優' in model_name")
    
    # 從篩選後的模型中隨機選擇一個
    selected_model = random.choice(filtered_models)
    
    model_name = selected_model["model_name"]
    print('Selected model:', model_name)
   
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