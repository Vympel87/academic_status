from pydantic import BaseModel
from typing import Any

# Request Schema
class ClassificationRequest(BaseModel):
    name: str
    gpa: float
    attendance: float

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
