import random
from ai_image.sd_api import SDClient
    
def get_model():
    """
    取得模型名稱
    """
    return "best_meinaunreal_v1Beta"
    
def get_random_model():
    """
    隨機選擇模型
    """
    # 獲取可用模型列表
    models = SDClient.get_models()
    filtered_models = [model for model in models if "best" in model["model_name"]]
    
    # 檢查是否有符合條件的模型
    if not filtered_models:
        raise Exception("No models found with '較優' in model_name")
    
    # 從篩選後的模型中隨機選擇一個
    selected_model = random.choice(models)
    return selected_model["model_name"]
       