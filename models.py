from pydantic import BaseModel
from pydantic import BaseModel
from typing import List, Optional
from typing import List
class LabTest(BaseModel):
    test_name: str
    test_value: str
    bio_reference_range: str
    test_unit: str
    lab_test_out_of_range: bool


# Response schema
class LabTestResponse(BaseModel):
    is_success: bool
    data: List[LabTest]
    error: Optional[str] = None