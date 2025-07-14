# utils/ocr_wrapper.py

import logging

import easyocr
import numpy as np
from PIL import Image

# Initialize once
_easyocr_reader = easyocr.Reader(['en'])


def read_text(image: Image.Image) -> dict:
    """Run EasyOCR on an image and return combined text and confidence."""
    try:
        result = _easyocr_reader.readtext(np.array(image))
        text = " ".join([r[1] for r in result])
        confs = [r[2] for r in result]
        avg_conf = sum(confs) / len(confs) if confs else 0
        return {"engine": "easyocr", "text": text, "confidence": avg_conf}
    except Exception as e:
        logging.error(f"❌ EasyOCR failed: {e}")
        return {"engine": "easyocr", "text": "", "confidence": 0}
