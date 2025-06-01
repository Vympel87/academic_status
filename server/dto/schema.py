from pydantic import BaseModel, Field
from typing import Any

# Request Schema
class ClassificationRequest(BaseModel):
    gpa: float
    marital_status: str = Field(..., alias="Marital status")
    application_mode: str = Field(..., alias="Application mode")
    daytime_evening_attendance: str = Field(..., alias="Daytime/evening attendance")
    previous_qualification: str = Field(..., alias="Previous qualification")
    mothers_qualification: str = Field(..., alias="Mother's qualification")
    fathers_qualification: str = Field(..., alias="Father's qualification")
    mothers_occupation: str = Field(..., alias="Mother's occupation")
    fathers_occupation: str = Field(..., alias="Father's occupation")
    displaced: str = Field(..., alias="Displaced")
    debtor: str = Field(..., alias="Debtor")
    tuition_fees_up_to_date: str = Field(..., alias="Tuition fees up to date")
    gender: str = Field(..., alias="Gender")
    scholarship_holder: str = Field(..., alias="Scholarship holder")

# Response Data Schema (isinya bagian "data" dari success response)
class ClassificationData(BaseModel):
    status: str
    confidence: float

# Response Schema (Success + Error)

# Success response dengan generic data field
class SuccessResponse(BaseModel):
    status: str = "success"
    data: Any

# Error response
class ErrorResponse(BaseModel):
    status: str = "failed"
    message: str
