from dto.schema import ClassificationRequest, ClassificationData
from util.helper import predict_student_status

class ClassificationService:
    @staticmethod
    async def predict(payload: ClassificationRequest) -> ClassificationData:
        try:
            # Ubah payload menjadi dict
            input_data = payload.dict()
            
            # Panggil helper predict
            status, confidence = predict_student_status(input_data)

            return ClassificationData(
                status=status,
                confidence=confidence
            )
        except Exception as e:
            # Bubble error ke controller supaya tertangkap di response 500
            raise Exception(f"Prediction failed: {str(e)}")
