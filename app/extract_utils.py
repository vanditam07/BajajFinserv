import re
from typing import List, Dict, Any
from app.models import LabTest
from .exceptions import ExtractionException
from .config import TEST_PATTERNS, REFERENCE_RANGES

def extract_lab_test_data(ocr_text: str) -> List[Dict[str, Any]]:
    ocr_text = re.sub(r'\s+', ' ', ocr_text)
    ocr_text = ocr_text.upper()
    print("Preprocessed OCR Text:", ocr_text)
    lab_tests = []
    tests = extract_with_patterns(ocr_text)
    if not tests:
        raise ExtractionException("No lab test data found in the OCR text.")
    for test in tests:
        test_name = test['test_name']
        test_value = test['test_value']
        test_unit = test['test_unit'] or "N/A"
        bio_reference_range = test['bio_reference_range']
        try:
            ref_parts = re.findall(r"[\d.-]+", bio_reference_range)
            if len(ref_parts) >= 2:
                ref_min, ref_max = map(float, ref_parts[:2])
                try:
                    test_value_float = float(test_value)
                    lab_test_out_of_range = test_value_float < ref_min or test_value_float > ref_max
                except ValueError:
                    lab_test_out_of_range = False
            else:
                lab_test_out_of_range = False
        except (ValueError, TypeError):
            lab_test_out_of_range = False
        lab_tests.append({
            "test_name": test_name,
            "test_value": test_value,
            "bio_reference_range": bio_reference_range,
            "test_unit": test_unit,
            "lab_test_out_of_range": lab_test_out_of_range
        })
    return lab_tests

def extract_with_patterns(text: str) -> List[Dict]:
    tests = []
    for pattern in TEST_PATTERNS:
        matches = re.finditer(pattern, text, re.IGNORECASE | re.VERBOSE)
        for match in matches:
            test_name = match.group('name').strip()
            test_value = clean_value(match.group('value'))
            unit = match.groupdict().get('unit', "").strip()
            ref_range = match.groupdict().get('range') or REFERENCE_RANGES.get(test_name.upper(), "N/A")
            tests.append({
                "test_name": test_name,
                "test_value": test_value,
                "bio_reference_range": ref_range,
                "test_unit": unit,
                "lab_test_out_of_range": is_out_of_range(test_value, ref_range)
            })
    return tests

def clean_value(value: str) -> str:
    value = value.strip()
    value = re.sub(r'[^\d.]', '', value)
    return value

def is_out_of_range(value: str, ref_range: str) -> bool:
    try:
        val = float(value)
        if ref_range == "N/A":
            return False
        if "-" in ref_range:
            parts = ref_range.split("-")
            if len(parts) >= 2:
                lower = float(parts[0].strip())
                upper = float(parts[1].strip())
                return val < lower or val > upper
        return False
    except ValueError:
        return False
