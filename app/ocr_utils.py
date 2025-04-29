import cv2
import numpy as np
from PIL import Image
import io
from .exceptions import OCRException
from .config import OCR_CONFIG
import easyocr

def process_image(image_bytes: bytes) -> np.ndarray:
    try:
        image = Image.open(io.BytesIO(image_bytes))
        img_np = np.array(image)
        gray = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
        processed = gray
        if OCR_CONFIG.get('denoise', True):
            processed = cv2.fastNlMeansDenoising(processed, h=30)
        if OCR_CONFIG.get('sharpen', True):
            kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
            processed = cv2.filter2D(processed, -1, kernel)
        if OCR_CONFIG.get('threshold', True):
            processed = cv2.adaptiveThreshold(
                processed, 255,
                cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                cv2.THRESH_BINARY, 31, 10
            )
        return processed
    except Exception as e:
        raise OCRException(f"Image processing failed: {e}")

def extract_text(image_np: np.ndarray) -> str:
    try:
        reader = easyocr.Reader([OCR_CONFIG.get('lang', 'en')])
        result = reader.readtext(image_np)
        extracted_text = " ".join([text[1] for text in result])
        return extracted_text
    except Exception as e:
        raise OCRException(f"OCR failed using EasyOCR: {e}")
