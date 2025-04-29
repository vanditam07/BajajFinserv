from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from PIL import Image, UnidentifiedImageError
import numpy as np
import io
from app.ocr_utils import extract_text
from app.extract_utils import extract_lab_test_data

app = FastAPI(
    title="Lab Report OCR API",
    description="Extract lab test data from uploaded images of lab reports."
)

class LabTest(BaseModel):
    test_name: str
    test_value: str
    bio_reference_range: str
    test_unit: str
    lab_test_out_of_range: bool

class LabTestResponse(BaseModel):
    is_success: bool
    data: Optional[List[LabTest]] = None
    error: Optional[str] = None

@app.post("/get-lab-tests", response_model=LabTestResponse)
async def get_lab_tests(file: UploadFile = File(...)):
    try:
        if file.content_type not in ["image/jpeg", "image/png", "image/jpg"]:
            raise HTTPException(status_code=400, detail="Invalid file type. Only JPEG and PNG images supported.")
        contents = await file.read()
        image = Image.open(io.BytesIO(contents)).convert("RGB")
        image_np = np.array(image)
        text = extract_text(image_np)
        lab_tests_data = extract_lab_test_data(text)
        if not isinstance(lab_tests_data, list):
            lab_tests_data = [lab_tests_data] if lab_tests_data else []
        lab_tests = [LabTest(**test_data) for test_data in lab_tests_data]
        return LabTestResponse(is_success=True, data=lab_tests)
    except UnidentifiedImageError:
        raise HTTPException(status_code=400, detail="Uploaded file is not a valid image.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return LabTestResponse(is_success=False, error=str(e))

@app.get("/")
def root():
    return {"message": "Welcome to the Lab Report OCR API!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
