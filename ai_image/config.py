# config.py

import difflib
import json

MODEL_LIST_URL = "http://127.0.0.1:7860/sdapi/v1/sd-models"
GENERATE_IMAGE_URL = "http://127.0.0.1:7860/sdapi/v1/txt2img"
OUTPUT_DIR = "src/test"

class BaseConfig:
    """Configuration for basic parameters."""
    def __init__(self):
        self.prompt = "((masterpiece)), (best quality), beautiful, photography, 8K, HDR, highres, absurdres:1.2, ultra-detailed, (vibrant color:1.2), ambient light, perfect lighting, textured skin, extremely detailed face, beautiful detailed face, beautiful detailed eyes, beautiful detailed pupils, detailed background, 1girl, cute, (Kpop idol), rebecca \(cyberpunk\), solo, colored skin, white skin, (green hair:0.7), multicolor hair, very long hair, small breasts, red pupils,multicolor pupils ,cowboy shot, tilted down, solo, female, nude, naked, thighs, breasts, multicolor, thong, navel, thicc, <lora:rebeccaCyberpunk_v10:0.8>, (family friendly:0.5)emotions"
        self.negative_prompt = "(worst quality:2), (low quality:2), (normal quality:2), ((monochrome)), ((grayscale)),paintings, sketches, normal quality, lowres, lens flare, text, artist name, username, (bad anatomy), nsfw, black bra"
        self.styles = []
        self.seed = -1
        self.sampler_name = "DPM++ 2M SDE Karras"
        self.batch_size = 1
        self.n_iter = 1
        self.steps = 20
        self.cfg_scale = 7
        self.height = 512
        self.width = 768
        self.restore_faces = True
        self.tiling = False

class HighResConfig:
    """Configuration for high-resolution parameters."""
    def __init__(self):
        self.enable_hr = True
        self.hr_scale = 2
        self.hr_upscaler = "R-ESRGAN 4x+"
        self.hr_second_pass_steps = 20
        self.firstphase_width = 0
        self.firstphase_height = 0
        self.hr_resize_x = 0
        self.hr_resize_y = 0
        self.hr_checkpoint_name = ""
        self.hr_sampler_name = ""
        self.hr_prompt = ""
        self.hr_negative_prompt = ""

class PostProcessingConfig:
    """Configuration for post-processing parameters."""
    def __init__(self):
        self.postprocessing = {
            "postprocess_upscale_by": 2,
            "postprocess_upscaler": "R-ESRGAN 4x+"
        }
        self.extras = {
            "postprocess_upscale_by": 2,
            "postprocess_upscaler": "R-ESRGAN 4x+"
        }

class OtherConfig:
    """Configuration for other parameters."""
    def __init__(self):
        self.override_settings = {
            "sd_model_checkpoint": "best_meinaunreal_v1Beta"
        }
        self.disable_extra_networks = False
        self.script_name = ""
        self.script_args = []
        self.send_images = True
        self.save_images = False
        self.alwayson_scripts = {}
        
class ParamsConfig:
    """Main configuration class combining all configurations."""
    def __init__(self):
        self.base = BaseConfig()
        self.high_res = HighResConfig()
        self.post_processing = PostProcessingConfig()
        self.other = OtherConfig()

    def to_dict(self):
        """Convert the entire configuration to a dictionary."""
        result = vars(self.base).copy()
        result.update(vars(self.high_res))
        result.update(vars(self.post_processing))
        # result.update(vars(self.other))
        result["override_settings"] = self.other.override_settings
        return result

    def update(self, custom_params):
        """Update parameters with custom values."""
        if not isinstance(custom_params, dict):
            raise ValueError("Custom parameters must be a dictionary.")
        for key, value in custom_params.items():
            if key in self.to_dict():
                if isinstance(self.to_dict()[key], dict) and isinstance(value, dict):
                    # 更新嵌套字典
                    self.to_dict()[key].update(value)
                else:
                    setattr(self, key, value)
            else:
                suggestions = difflib.get_close_matches(key, self.to_dict().keys())
                suggestion_msg = f" Did you mean: {', '.join(suggestions)}?" if suggestions else ""
                print(f"Warning: {key} is not a recognized parameter.{suggestion_msg}")
                
    def print_config(self):
        """Print the entire configuration."""
        from pprint import pprint
        pprint(self.to_dict())

    def reset(self):
        """Reset all configurations to their default values."""
        self.__init__()
        
    def save_to_json(self, filepath):
        """Save configuration to a JSON file."""
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f, indent=4)

    def load_from_json(self, filepath):
        """Load configuration from a JSON file."""
        with open(filepath, "r", encoding="utf-8") as f:
            custom_params = json.load(f)
        self.update(custom_params)
        
    def reset_param(self, key):
        """Reset a single parameter to its default value."""
        default_config = ParamsConfig()  # Create a fresh instance
        if hasattr(self.base, key):
            setattr(self.base, key, getattr(default_config.base, key))
        else:
            print(f"Warning: {key} is not a recognized parameter.")

        
if __name__ == "__main__":
    params_config = ParamsConfig()
    params_config.save_to_json("config.json")  # 保存到文件
    params_config.load_from_json("config.json")  # 從文件加載
    params_config.reset_param("width")

    # 查看預設配置
    print("Default Configuration:")
    params_config.print_config()

    # 自定義更新
    custom_params = {
        "base": {
            "height": 1024,
            "width": 1024
        },
        "high_res": {
            "enable_hr": False
        }
    }
    params_config.update(custom_params)

    print("\nUpdated Configuration:")
    params_config.print_config()

    # 重置配置
    params_config.reset()
    print("\nReset Configuration:")
    params_config.print_config()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
DEFAULT_PARAMS = {
    "prompt": "",
    "negative_prompt": "",
    "styles": [],
    "seed": -1,
    "subseed": -1,
    "subseed_strength": 0,
    "seed_resize_from_h": -1,
    "seed_resize_from_w": -1,
    "sampler_name": "DPM++ 2M SDE Karras",
    "batch_size": 1,
    "n_iter": 1,
    "steps": 20,
    "cfg_scale": 7,
    "height": 512,
    "width": 512,
    "restore_faces": True,
    "tiling": False,
    "do_not_save_samples": False,
    "do_not_save_grid": False,
    "eta": 0,
    "denoising_strength": 0.5,
    "s_min_uncond": 0,
    "s_churn": 0,
    "s_tmax": 0,
    "s_tmin": 0,
    "s_noise": 0,
    "override_settings_restore_afterwards": True,
    "refiner_checkpoint": "",
    "refiner_switch_at": 0,
    "disable_extra_networks": False,
    "comments": {},
    "enable_hr": True,
    "firstphase_width": 0,
    "firstphase_height": 0,
    "hr_scale": 2,
    "hr_upscaler": "R-ESRGAN 4x+",
    "hr_second_pass_steps": 20,
    "hr_resize_x": 0,
    "hr_resize_y": 0,
    "hr_checkpoint_name": "",
    "hr_sampler_name": "",
    "hr_prompt": "",
    "hr_negative_prompt": "",
    "sampler_index": "DPM++ 2M SDE Karras",
    "script_name": "",
    "script_args": [],
    "send_images": True,
    "save_images": False,
    "alwayson_scripts": {},
    "postprocessing": {
        "postprocess_upscale_by": 2,
        "postprocess_upscaler": "R-ESRGAN 4x+"
    },
    "extras": {
        "postprocess_upscale_by": 2,
        "postprocess_upscaler": "R-ESRGAN 4x+"
    },
    "override_settings": {
        "sd_model_checkpoint": ""
    }
}
