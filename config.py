# OCR Configuration
# OCR Configuration
OCR_CONFIG = {
    'denoise': True,  # Denoise image for better OCR accuracy
    'sharpen': True,  # Sharpen image to highlight text edges
    'threshold': True,  # Apply thresholding for better contrast
    'lang': 'en',  # Use English as the OCR language
    'oem': 3,  # OCR Engine Mode (default is 3, use LSTM-based OCR)
    'psm': 6,  # Page Segmentation Mode (ideal for block of text)
}

TEST_PATTERNS = [
    # Pattern 1: Test Name Value [Range] Unit
    r"""
    (?P<name>[A-Z][A-Z\s\/\-]+)\s*               # Test Name: All caps with spaces/slashes
    (?P<value>\d+\.?\d*)\s*                      # Value: Number with optional decimal
    (?:\[?\(?\s*(?P<range>\d+\.?\d*\s*-\s*\d+\.?\d*)\s*\]?\)?)?\s*  # Optional Range
    (?P<unit>[A-Z%\/]*)                          # Optional unit
    """
,

    # Pattern 2: Test Name: Value Unit (Range)
    r"""
    (?P<name>[A-Z][A-Z\s\/\-]+):\s*               # Test Name
    (?P<value>\d+\.?\d*)\s*                       # Value
    (?P<unit>[A-Z%\/]*)\s*                        # Optional Unit
    (?:\(?\s*(?P<range>\d+\.?\d*\s*-\s*\d+\.?\d*)\s*\)?)?  # Optional Range
    """

]
# Standard reference ranges for common tests
REFERENCE_RANGES = {
    "HB": "12.0-15.0",        # Hemoglobin Range
    "HEMOGLOBIN": "12.0-15.0", # Hemoglobin alternative name
    "PCV": "36.0-46.0",       # Packed Cell Volume Range
    "WBC": "4000-11000"        # White Blood Cells Count Range
    # Extend as needed for other tests
}