from src.models import ImageEnhancer
from src.utils import pil_to_bgr, bgr_to_pil, load_image
from src.ui import (
    render_header,
    render_file_uploader,
    render_instructions,
    render_interative_slider,
    render_downloader_button

    
)
import streamlit as st
from config import PAGE_CONFIG
st.set_page_config(**PAGE_CONFIG)


def main():
    "funcion aplicacion"
    render_header()

    #Inicializar el modelo
    enhacer = ImageEnhancer()
    st.success("Modelos Listos")

    #Subir fichero
    uploaded_file 

if __name__ == "__main__":
    main()

