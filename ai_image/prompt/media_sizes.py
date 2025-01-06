import random

from ai_image.prompt.data.social_media_sizes import SOCIAL_MEDIA_SIZES

class SocialMediaImageSizes:
    """Class to manage and retrieve image sizes for various social media platforms."""
    def __init__(self):
        self.sizes = SOCIAL_MEDIA_SIZES

    def get_size(self, platform, image_type):
        """Retrieve the image size for a specific platform and image type."""
        if platform not in self.sizes:
            raise ValueError(f"Platform '{platform}' not found.")
        if image_type not in self.sizes[platform]:
            raise ValueError(f"Image type '{image_type}' not found for platform '{platform}'.")
        return self.sizes[platform][image_type]

    def get_random_size(self):
        """Retrieve a random image size from any platform and type."""
        platform = random.choice(list(self.sizes.keys()))
        image_type = random.choice(list(self.sizes[platform].keys()))
        size = self.sizes[platform][image_type]
        return platform, image_type, size
    
# Example Usage
if __name__ == "__main__":
    image_sizes = SocialMediaImageSizes()

    # Example: Get the size for an Instagram story
    platform = "Instagram"
    image_type = "story"
    try:
        size = image_sizes.get_size(platform, image_type)
        print(f"The size for {platform} {image_type} is: {size}")
    except ValueError as e:
        print(e)

    # Example: Get the size for a Facebook cover photo
    platform = "Facebook"
    image_type = "cover_photo"
    try:
        size = image_sizes.get_size(platform, image_type)
        print(f"The size for {platform} {image_type} is: {size}")
    except ValueError as e:
        print(e)

    # Example: Get a random image size
    platform, image_type, size = image_sizes.get_random_size()
    print(f"Randomly selected size: {platform} {image_type} is: {size}")