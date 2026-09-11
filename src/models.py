from gfpgan import GFPGANer
from config import CONFIG
from zeroscratches.erase_scratches import EraseScratches
from src.utils import bgr_to_pil, pil_to_bgr
import streamlit as st

class ImageEnhancer:
    """Class use for model GEPGAN"""
    def __init__(self):
        self.model = None
        self._scratch_eraser = None

    @property
    def scratch_eraser(self):
        if self._scratch_eraser is None:
            self._scratch_eraser = EraseScratches()
        return self._scratch_eraser

    def _remove_scratches(self, image_bgr):
        """Elimina las rayas o grietas antes de pasar a GEPGAN"""
        pil_img = bgr_to_pil(image_bgr)
        restored_rgb = self.scratch_eraser.erase(pil_img)
        restored_bgr = pil_to_bgr(restored_rgb)
        return restored_bgr

    @st.cache_resource
    def load_model_simple(_self):
        """GEPGAN only head"""
        model = GFPGANer(
            model_path=CONFIG["model_url"],
            upscale=CONFIG["upscale"],
            arch=CONFIG["arch"],
            channel_multiplier=CONFIG["channel_multiplier"],
            bg_upsampler=None #fondo

        )
        return model

    def enhance(self, image_bgr, repair_scratches=False):
        """ mejorar la imagen con opciones de configuracion
        args: image_bgr: imagen en formato bgr blue,gree,red
        """
        if repair_scratches == True:
            st.info('Reparando grietas...')
            image_bgr = self._remove_scratches(image_bgr)
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
