from pydantic import BaseModel, Field
from typing import Any

# Request Schema
class ClassificationRequest(BaseModel):
    curricular_units_2nd_sem_approved: int = Field(..., alias="Curricular units 2nd sem (approved)")
    curricular_units_2nd_sem_grade: float = Field(..., alias="Curricular units 2nd sem (grade)")
    curricular_units_1st_sem_approved: int = Field(..., alias="Curricular units 1st sem (approved)")
    curricular_units_1st_sem_grade: float = Field(..., alias="Curricular units 1st sem (grade)")
    tuition_fees_up_to_date: str = Field(..., alias="Tuition fees up to date")
    scholarship_holder: str = Field(..., alias="Scholarship holder")
    age_at_enrollment: int = Field(..., alias="Age at enrollment")
    debtor: str = Field(..., alias="Debtor")
    gender: str = Field(..., alias="Gender")
    application_mode: str = Field(..., alias="Application mode")
    curricular_units_2nd_sem_evaluations: int = Field(..., alias="Curricular units 2nd sem (evaluations)")
    curricular_units_2nd_sem_enrolled: int = Field(..., alias="Curricular units 2nd sem (enrolled)")
    curricular_units_1st_sem_enrolled: int = Field(..., alias="Curricular units 1st sem (enrolled)")
    curricular_units_1st_sem_evaluations: int = Field(..., alias="Curricular units 1st sem (evaluations)")
    admission_grade: float = Field(..., alias="Admission grade")
    displaced: str = Field(..., alias="Displaced")
    previous_qualification_grade: float = Field(..., alias="Previous qualification (grade)")
    curricular_units_2nd_sem_without_evaluations: int = Field(..., alias="Curricular units 2nd sem (without evaluations)")
    marital_status: str = Field(..., alias="Marital status")
    application_order: int = Field(..., alias="Application order")
    daytime_evening_attendance: str = Field(..., alias="Daytime/evening attendance")
    mothers_qualification: str = Field(..., alias="Mother's qualification")
    curricular_units_1st_sem_without_evaluations: int = Field(..., alias="Curricular units 1st sem (without evaluations)")
    curricular_units_2nd_sem_credited: int = Field(..., alias="Curricular units 2nd sem (credited)")
    mothers_occupation: str = Field(..., alias="Mother's occupation")
    fathers_occupation: str = Field(..., alias="Father's occupation")
    curricular_units_1st_sem_credited: int = Field(..., alias="Curricular units 1st sem (credited)")
    previous_qualification: str = Field(..., alias="Previous qualification")
    fathers_qualification: str = Field(..., alias="Father's qualification")

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
