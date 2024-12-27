# config.py

import difflib
import json

# get
SD_API_BASE_URL = "http://127.0.0.1:7860"
MODEL_LIST_URL = "/sdapi/v1/sd-models"
CONFIG_URL = "/sdapi/v1/config"
SAMPLER_LIST_URL = "/sdapi/v1/samplers"
UPSCALER_LIST_URL = "/sdapi/v1/upscalers"
LORA_LIST_URL = "/sdapi/v1/loras"

#post
GENERATE_IMAGE_URL = "http://127.0.0.1:7860/sdapi/v1/txt2img"

# output
OUTPUT_DIR = "src/test"

class BaseConfig:
    """Configuration for basic parameters."""
    def __init__(self):
        self.prompt = "((masterpiece)), (best quality), beautiful, photography, 8K, HDR, highres, absurdres:1.2, ultra-detailed, (vibrant color:1.2), ambient light, perfect lighting, textured skin, extremely detailed face, beautiful detailed face, beautiful detailed eyes, beautiful detailed pupils, detailed background, 1girl, cute, (Kpop idol), rebecca \(cyberpunk\), solo, colored skin, white skin, (green hair:0.7), multicolor hair, very long hair, small breasts, red pupils,multicolor pupils ,cowboy shot, tilted down, solo, female, nude, naked, thighs, breasts, multicolor, thong, navel, thicc, <lora:rebeccaCyberpunk_v10:0.8>, (family friendly:0.5)emotions" # 正面提示，用於引導生成圖像的主題和細節。
        self.negative_prompt = "(worst quality:2), (low quality:2), (normal quality:2), ((monochrome)), ((grayscale)),paintings, sketches, normal quality, lowres, lens flare, text, artist name, username, (bad anatomy), nsfw, black bra"  # 負面提示，用於避免不希望出現的內容。
        self.styles = []  # 圖像風格列表，應用預定義的風格。
        self.seed = -1  # 隨機種子，-1 表示隨機生成。
        self.seed_resize_from_h = -1  # 隨機種子生成時的高度調整（像素），-1 表示禁用。
        self.seed_resize_from_w = -1  # 隨機種子生成時的寬度調整（像素），-1 表示禁用。
        self.eta = 0  # 採樣器的 eta 值，控制生成過程的隨機性。
        self.denoising_strength = 0.5  # 降噪強度，用於高分辨率處理時調整生成細節。
        self.sampler_name = "DPM++ 2M SDE Karras"  # 採樣器名稱，控制生成方式。
        self.sampler_index = "DPM++ 2M SDE Karras"  # 採樣器索引，可能是內部使用的參數。
        self.batch_size = 1  # 每批生成的圖像數量。
        self.n_iter = 1  # 生成的迭代次數。
        self.steps = 20  # 採樣步驟數量，越高生成細節越多但速度越慢。
        self.cfg_scale = 7  # 引導比例，用於平衡提示語與隨機生成內容的影響。
        self.height = 512  # 圖像高度（像素）。
        self.width = 768  # 圖像寬度（像素）。
        self.restore_faces = True  # 是否啟用面部修復功能。
        self.tiling = False  # 是否啟用平鋪模式（生成無縫圖像）。
        self.subseed = -1  # 子隨機種子，用於變化主隨機種子生成的內容。
        self.subseed_strength = 0  # 子隨機種子的影響程度。
        self.postprocess_upscaler = "R-ESRGAN 4x+"  # 後處理的放大器名稱。

class HighResConfig:
    """Configuration for high-resolution parameters."""
    def __init__(self):
        self.enable_hr = True  # 是否啟用高分辨率處理。
        self.hr_scale = 2  # 高分辨率放大比例。
        self.hr_upscaler = "R-ESRGAN 4x+"  # 高分辨率放大器名稱。
        self.hr_second_pass_steps = 20  # 高分辨率生成的採樣步驟數量。
        self.firstphase_width = 0  # 第一階段生成的寬度（像素），0 表示與主圖像一致。
        self.firstphase_height = 0  # 第一階段生成的高度（像素），0 表示與主圖像一致。
        self.hr_resize_x = 0  # 高分辨率模式下，水平調整的目標像素數，0 表示不調整。
        self.hr_resize_y = 0  # 高分辨率模式下，垂直調整的目標像素數，0 表示不調整。
        self.hr_checkpoint_name = ""  # 用於高分辨率生成的模型名稱（可選）。
        self.hr_sampler_name = ""  # 用於高分辨率生成的採樣器名稱（可選）。
        self.hr_prompt = ""  # 高分辨率階段的正面提示（可選）。
        self.hr_negative_prompt = ""  # 高分辨率階段的負面提示（可選）。

class PostProcessingConfig:
    """Configuration for post-processing parameters."""
    def __init__(self):
        self.postprocessing = {
            "postprocess_upscale_by": 2,  # 圖像放大的倍數（後處理）。
            "postprocess_upscaler": "R-ESRGAN 4x+"  # 放大器名稱（後處理）。
        }
        self.extras = {
            "postprocess_upscale_by": 2,  # 圖像放大的倍數（附加功能）。
            "postprocess_upscaler": "R-ESRGAN 4x+"  # 放大器名稱（附加功能）。
        }

class OtherConfig:
    """Configuration for other parameters."""
    def __init__(self):
        self.override_settings = {
            "sd_model_checkpoint": "best_meinaunreal_v1Beta"  # 指定使用的模型名稱。
        }
        self.override_settings_restore_afterwards = True  # 使用完後恢復設置。
        self.disable_extra_networks = False  # 是否禁用額外的網絡（如插件模型）。
        self.script_name = ""  # 自定義腳本名稱（可選）。
        self.script_args = []  # 自定義腳本參數（可選）。
        self.send_images = True  # 是否返回生成的圖像。
        self.save_images = True  # 是否保存生成的圖像。
        self.do_not_save_samples = True  # 是否禁用保存中間樣本。
        self.do_not_save_grid = True  # 是否禁用保存圖像網格。
        self.alwayson_scripts = {}  # 始終啟用的腳本（如預處理插件）。
        
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
