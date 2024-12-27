# main.py

from ai_image.sd_api import SDClient

if __name__ == '__main__':
    # Fetch and print models
    models = SDClient.get_models()
    print("Available Models:")
    for model in models:
        print(f"Model Name: {model.get('model_name')}")

    # Fetch and print samplers
    samplers = SDClient.get_samplers()
    print("\nAvailable Samplers:")
    for sampler in samplers:
        print(f"Sampler Name: {sampler.get('name')}")

    # Fetch and print upscalers
    upscalers = SDClient.get_upscalers()
    print("\nAvailable Upscalers:")
    for upscaler in upscalers:
        print(f"Upscaler Name: {upscaler.get('name')}")

    # Fetch and print LoRAs
    loras = SDClient.get_loras()
    print("\nAvailable LoRAs:")
    for lora in loras:
        print(f"LoRA Name: {lora.get('name')}")
