import uuid
from models import fetch_models
from image_generator import generate_image, save_image, ensure_output_dir
from utils import get_generate_params

OUTPUT_DIR = "generated_images"

def main():
    generate_params = get_generate_params()

    # 創建輸出目錄
    ensure_output_dir(OUTPUT_DIR)

    # 獲取可用模型列表
    models = fetch_models()

    # 遍歷每個模型並生成圖片
    for model in models:
        model_name = model["model_name"]
        print(f"Generating image with model: {model_name}")

        # try:
        images = generate_image(model_name, generate_params)
        for i, img in enumerate(images):
            image_filename = f"{OUTPUT_DIR}/{uuid.uuid4().hex}{model_name}_{i}.png"
            save_image(img, image_filename)
        print(f"Image generated and saved for model: {model_name}")
        # except Exception as e:
        #     print(e)

    print("Done generating images with all models.")

if __name__ == "__main__":
    main()
