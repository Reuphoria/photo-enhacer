from src.models import ImageEnhancer
from src.utils import pil_to_bgr, bgr_to_pil, load_image

def main():
    # cargar una imagen como PIL usando la funcion auxiliar
    with open('C:\\Users\\Ricardo Meneses\\Documents\\Proyecto_Git\\photo-enhacer\\imagen1.jpg', "rb") as f:
        image_pil = load_image(f)

    # convertir de pil a bgr
    image_bgr = pil_to_bgr(image_pil)

    # crear el odjeto enhancer y restaurar
    enhancer = ImageEnhancer()
    restored_bgr = enhancer.enhance(image_bgr)

    #convertir de BGR a PIL
    restored_pil = bgr_to_pil(restored_bgr)

    #guardar la imagen en disco
    restored_pil.save("C:\\Users\\Ricardo Meneses\\Documents\\Proyecto_Git\\photo-enhacer\\imagen1_restored.jpg")

if __name__ == "__main__":
    main()