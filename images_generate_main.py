
from ai_image.prompt.param import adjust_params
from ai_image.save_images import ImageOperations
from ai_image.txt_to_img import generate_images
from file.utils import generate_time_based_filename

def generate_and_save_images():
    generate_params = adjust_params()

    images = generate_images(generate_params)
    ImageOperations.save_images(images, generate_params, generate_time_based_filename)

def main():
    # for num in range(1, 100):
        generate_and_save_images()

if __name__ == "__main__":
    main()
