import pytesseract
import cv2

def extract_table_data(image_np):
    """Extract data from tables using pytesseract"""
    data = pytesseract.image_to_data(image_np, output_type=pytesseract.Output.DICT)
    
    table = []
    for i in range(len(data['text'])):
        if int(data['conf'][i]) > 60:  
            table.append(data['text'][i])
    
    return table
