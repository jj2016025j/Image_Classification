from generated_images.image_generator import generate_images
from generated_images.save_images import save_images
from prompt.prompt import adjust_params

def generate_and_save_images():
    generate_params = adjust_params()

    images = generate_images(generate_params)

    save_images(images, generate_params)

def main():
    for num in range(1, 100):
        generate_and_save_images()

if __name__ == "__main__":
    main()
