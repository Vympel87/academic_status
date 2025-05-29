from fastapi import APIRouter
from fastapi.responses import JSONResponse
from dto.schema import ClassificationRequest, ClassificationData, SuccessResponse, ErrorResponse
from service.classification_service import ClassificationService

router = APIRouter(
    prefix="/api/ml",
    tags=["Machine Learning"],
)

@router.post("/classify", response_model=SuccessResponse, responses={500: {"model": ErrorResponse}})
async def classify_data(payload: ClassificationRequest):
    try:
        result = await ClassificationService.predict(payload)
        return SuccessResponse(data=result)
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content=ErrorResponse(message=str(e)).dict()
        )
