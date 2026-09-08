import streamlit as st
from config import CONFIG
from PIL import Image
import numpy as np
import cv2
import io
#mostrar cabecera
def render_header():
    """cabecera"""
    st.title("Mejora La Calidad de Tus Fotos")
    st.markdown("Sube una foto y mejora la calidad de tu foto con IA usando GEPGAN")

def render_file_uploader():
    """
    cargar los archivos:
    return:
        Uploadedfile o none
    """
    uploaded_file = st.file_uploader(
        "Seleccioa una imagen",
        type=CONFIG['allowed_formats'],
        help="Sube una foto para mejorar la calidad"
    )
    return uploaded_file

def render_interative_slider(original_image, restored_image):
    """
    renderizar imagen:
    arg:
        original_image: PIL imagen original
        restored_image: PIL imagen restored
    """
    st.markdown("---")
    st.subheader("Comparador Interactivo")

    slider_value =st.slider(
        "Deslize para Comparar",
        min_value=0,
        max_value=100,
        value=50,
        label_visibility='collapsed'
    )

    #asegurar el tamano
    if original_image.size != restored_image.size:
        restored_image = restored_image.resize(original_image.size, Image.LANCZOS)

    #crear imagen dividida
    width = original_image.width
    split_pos = int(width * slider_value / 100)

    combined = Image.new('RGB', original_image.size)
    combined.paste(original_image.crop((0, 0, split_pos, original_image.height)), (0, 0))
    combined.paste(restored_image.crop((split_pos, 0, width, original_image.height)),(split_pos, 0))

    # añadir linea divisoria
    combined_array = np.array(combined)
    cv2.line(
        combined_array, # imagen
        (split_pos, 0), #linea en x1, y1
        (split_pos, combined.height), #punto final x2, y2
        (255,255,255), #color blanco
        3              #grosor
        )
    st.image(combined_array, width='stretch')

def render_downloader_button(restored_image):
    """renderizar imagen
       restored_image: imagen en PIL restored 
    """
    st.markdown('---')
    buf = io.BytesIO()
    restored_image.save(buf, format='PNG')
    st.download_button(
        label="Descargar Imagen Mejorada",
        data=buf.getvalue(),#odtener los datos
        file_name="Foto mejorada PNG",
        mime="image/png",
        width="stretch"
    )


def render_instructions():
    """Renderiza las instrucciones de uso."""
    st.info("👆 Sube una imagen para comenzar")
    
    with st.expander("ℹ️ ¿Cómo funciona?"):
        st.markdown("""
        1. **Sube una foto** usando el botón de arriba
        2. **Selecciona opciones** de procesamiento (opcional):
           - 🔧 **Reparar grietas**: Elimina rayas y arañazos
           - ✨ **Mejorar fondo**: Mejora calidad del fondo (más lento)
        3. **Haz clic en "Mejorar Calidad"** y espera unos segundos
        4. **Compara los resultados** con el slider interactivo
        5. **Descarga** tu foto mejorada
        
        **Ideal para:**
        - 📸 Fotos antiguas o de baja resolución
        - 👤 Retratos y selfies
        - 🖼️ Imágenes con caras borrosas
        - 🔧 Fotos con grietas o arañazos
        """)