def get_generate_params():
    return {
        "prompt": "(masterpiece, best quality, highres, ultra-detailed, 8k, 4k:1.4),(1girl, solo:1.4)",
        "negative_prompt": "(easynegative), (low quality:2), lowres, sketch, sketchby bad-artist, paintingby bad-artist, photographby bad-artist, traditional media, unfinished, abstract, signature, watermark, parody, oekaki, bad anatomy, bad hands, fewer digits, extra digit, missing arms, extra fingers, fewer fingers, extra leg, missing legs, wrong feet, wrong legs, (worst quality:2), (normal quality:2), (monochrome:1.21), (grayscale:1.21), skin spots, acnes, skin blemishes, age spot, glans, (fuze:1.4), (deformed:1.3), (malformed hands:1.4), (poorly drawn hands:1.4), (mutated fingers:1.4), (extra limbs:1.35)",
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
        "height": 768,
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
        }
    }
