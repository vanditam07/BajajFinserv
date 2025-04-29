OCR_CONFIG = {
    'denoise': True,
    'sharpen': True,
    'threshold': True,
    'lang': 'en',
    'oem': 3,
    'psm': 6,
}

TEST_PATTERNS = [
    r"""
    (?P<name>[A-Z][A-Z\s\/\-]+)\s*
    (?P<value>\d+\.?\d*)\s*
    (?:\[?\(?\s*(?P<range>\d+\.?\d*\s*-\s*\d+\.?\d*)\s*\]?\)?)?\s*
    (?P<unit>[A-Z%\/]*)
    """,
    r"""
    (?P<name>[A-Z][A-Z\s\/\-]+):\s*
    (?P<value>\d+\.?\d*)\s*
    (?P<unit>[A-Z%\/]*)\s*
    (?:\(?\s*(?P<range>\d+\.?\d*\s*-\s*\d+\.?\d*)\s*\)?)?
    """
]

REFERENCE_RANGES = {
    "HB": "12.0-15.0",
    "HEMOGLOBIN": "12.0-15.0",
    "PCV": "36.0-46.0",
    "WBC": "4000-11000"
}
