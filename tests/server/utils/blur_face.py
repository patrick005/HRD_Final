# utils/blur_face.py
import cv2
import numpy as np
from PIL import Image

def blur_face(pil_img):
    """
    중심 영역(얼굴 추정)에 Gaussian Blur 처리
    """
    cv_img = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
    h, w, _ = cv_img.shape
    x, y, bw, bh = w//3, h//4, w//3, h//5

    roi = cv_img[y:y+bh, x:x+bw]
    roi = cv2.GaussianBlur(roi, (99, 99), 30)
    cv_img[y:y+bh, x:x+bw] = roi
    
    return Image.fromarray(cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB))
