
from ai_image.prompt.param import adjust_params
from ai_image.save_images import ImageOperations
from ai_image.txt_to_img import generate_images
from file.utils import generate_filename_by_model

def generate_and_save_images():
    generate_params = adjust_params()
    images = generate_images(generate_params)
    
    model_name = generate_params["override_settings"]["sd_model_checkpoint"]
    filename = generate_filename_by_model(model_name)
    
    ImageOperations.save_images(images, generate_params, filename)

def main():
    for _ in range(1, 100):
        generate_and_save_images()

if __name__ == "__main__":
    main()
