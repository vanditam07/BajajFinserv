import pytesseract
import cv2

def extract_table_data(image_np):
    """Extract data from tables using pytesseract"""
    # Using pytesseract to extract table-like data
    data = pytesseract.image_to_data(image_np, output_type=pytesseract.Output.DICT)
    
    table = []
    for i in range(len(data['text'])):
        if int(data['conf'][i]) > 60:  # Only consider text with a certain confidence
            table.append(data['text'][i])
    
    return table
