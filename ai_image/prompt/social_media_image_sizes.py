import random

class SocialMediaImageSizes:
    """Class to manage and retrieve image sizes for various social media platforms."""
    def __init__(self):
        self.sizes = {
            "Facebook": {
                "profile_picture": (170, 170),
                "cover_photo": (820, 312),
                "post_image": (1200, 630),
                "ad_image_landscape": (1200, 628),
                "ad_image_square": (1080, 1080)
            },
            "Instagram": {
                "profile_picture": (110, 110),
                "post_square": (1080, 1080),
                "post_portrait": (1080, 1350),
                "post_landscape": (1080, 566),
                "story": (1080, 1920),
                "reels": (1080, 1920)
            },
            "Twitter": {
                "profile_picture": (400, 400),
                "cover_photo": (1500, 500),
                "post_image": (1200, 675)
            },
            "LinkedIn": {
                "profile_picture": (400, 400),
                "cover_photo": (1584, 396),
                "company_logo": (300, 300),
                "company_cover_photo": (1128, 191),
                "post_image": (1200, 627)
            },
            "YouTube": {
                "channel_logo": (800, 800),
                "channel_cover": (2560, 1440),
                "thumbnail": (1280, 720)
            },
            "TikTok": {
                "profile_picture": (200, 200),
                "video": (1080, 1920)
            },
            "Pinterest": {
                "profile_picture": (165, 165),
                "pin_image": (1000, 1500)
            },
            "Snapchat": {
                "ad": (1080, 1920),
                "spotlight_video": (1080, 1920)
            },
            "Reddit": {
                "profile_picture": (256, 256),
                "post_image": (1200, 628)
            }
        }

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