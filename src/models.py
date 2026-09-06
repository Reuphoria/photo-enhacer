from gfpgan import GFPGANer
from config import CONFIG


class ImageEnhancer:
    """Class use for model GEPGAN"""
    def __init__(self):
        self.model = None

    def load_model_simple(self):
        """GEPGAN only head"""
        model = GFPGANer(
            model_path=CONFIG["model_url"],
            upscale=CONFIG["upscale"],
            arch=CONFIG["arch"],
            channel_multiplier=CONFIG["channel_multiplier"],
            bg_upsampler=None #fondo

        )
        return model

    def enhance(self, image_bgr):
        """ mejorar la imagen con opciones de configuracion
        args: image_bgr: imagen en formato bgr blue,gree,red
        """
        if not self.model:
            self.model = self.load_model_simple()
        #1 valor: caras que a detectado
        #2 valor: caras restauradas
        #3 valor: imagen completa con cara restaurada
        _, _, restored_img = self.model.enhance(
            image_bgr,
            #False identificar las caras automaticamente 
            #True identificar manualmente
            has_aligned=False,
            #False: restaurar todas las caras 
            #True: la cara las centrada
            only_center_face=False,
            #False: solo devuelve las caras mejoradas sin el fondo
            #True: devolver las caras restauradas en pociciones originales
            paste_back=True,
            #0: cara original
            #1: cara IA no tan original
            weight=CONFIG["enhancement_weight"]
        )

        return restored_img
