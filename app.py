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
    uploaded_file = render_file_uploader()
    if uploaded_file is not None:
        original_image = load_image(uploaded_file)
        img_bgr = pil_to_bgr(original_image)

        #mostrar imagen original
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("original")
            st.image(original_image, width="stretch")

        #opciones de procesamiento
        st.markdown("---")
        st.subheader("⚙️ Opciones de Mejora")
                
        col_opt1, col_opt2 = st.columns(2)
        
        with col_opt1:
            repair_scratches = st.checkbox(
                "🔧 Reparar grietas",
                value=False,
                help="Elimina rayas y arañazos de la foto"
            )
        
        with col_opt2:
            enhance_background = st.checkbox(
                "✨ Mejorar calidad fondo",
                value=False,
                help="Usa RealESRGAN para mejorar el fondo (más lento)"
            )
        
        st.markdown("---")
        

        #Boton de procesamiento
        if st.button("Mejorar Calidad", type="primary", width="stretch"):
            with st.spinner("Procesando con IA GEPGAN"):
                #mejorar imagen
                restored_bgr = enhacer.enhance(
                    img_bgr,
                    repair_scratches=repair_scratches
                )
                restored_image = bgr_to_pil(restored_bgr)
                #estado de seccion stream lit
                #guardar
                st.session_state['restored_image'] = restored_image
                st.session_state['original_image'] = original_image

                st.success("Imagen Mejorada con Exito")
                st.rerun()
        #mostrar resultado
        if 'restored_image' in st.session_state:
            with col2:
                st.subheader("Mejorada")
                st.image(st.session_state['restored_image'], width="stretch")
            #comparador interactivo
            render_interative_slider(
                st.session_state['original_image'],
                st.session_state['restored_image']
            )
            #boton de descarga
            render_downloader_button(st.session_state['restored_image'])
    else:
        render_instructions()
if __name__ == "__main__":
    main()

