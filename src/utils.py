import cv2
import numpy as np
from PIL import Image



def pil_to_bgr(image):
    """
    convertir una imagen PIL a formato BGR(OpenCV)
    
    args:
        image: Image PIL
        retunr: array numpy BGR
    """
    #garanzar el formato imagen numpy
    img_array = np.array(image)
    img_bgr = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
    return img_bgr

def bgr_to_pil(image_bgr):
    """convertir una imagen de bgr(OpenCV) a pil
    arg:
        image_bgr: numpy array formato bgr
        return: imagen en pil
    """
    image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(image_rgb)
    return pil_image

def load_image(uploaded_file):
    """cargar imagen desde un archivo subido
    Arg:
        uploaded_file: Archivo subido desde Streamlit
        return: imagen en PIL en formato BGR
    """
    image = Image.open(uploaded_file).convert('RGB')
    return image
