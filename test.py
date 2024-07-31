from models import fetch_models


models = fetch_models()

for model in models:
    print(model['model_name'])