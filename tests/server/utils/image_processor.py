# utils/image_processor.py
from PIL import Image

def process_image(image):
    """
    이미지 기반으로 옷 추천 (임시 결과 반환)
    실제 환경에서는 OpenPose 결과와 함께 동작 가능
    """
    result = {
        "top": "black_tshirt",
        "bottom": "denim_jeans",
        "accessory": "none"
    }

    return image, result
