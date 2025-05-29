from dto.schema import ClassificationRequest, ClassificationData

class ClassificationService:
    @staticmethod
    async def predict(payload: ClassificationRequest) -> ClassificationData:
        # Test doang
        prediction = "Pass" if payload.gpa > 3.0 else "Fail"
        probability = 0.85

        return ClassificationData(
            status=prediction,
            confidence=probability
        )
