
CONFIG = {
    #modelo GEPGAN
    #release 
    "model_url": "https://github.com/TencentARC/GFPGAN/releases/download/v1.3.0/GFPGANv1.3.pth",
    "upscale": 2,
    "arch": "clean",
    "channel_multiplier": 2,
    #artificial a 0 a 1
    "enhancement_weight": 0.5,

    #ui
    #formato permitido
    "allowed_formats": ['jpg','jpeg','png']

    
}

PAGE_CONFIG = {
    "page_title": "Mejorador de Fotos con IA",
    "page_icon": "🚀",
    "layout": "centered"
}
