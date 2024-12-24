# config.py

MODELS_NAME = "較優"

# 預設參數
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