from util.feature_mapping import feature_mapping
import pandas as pd
import joblib

# Mapping dari snake_case ke nama alias sesuai model
alias_map = {
    "curricular_units_2nd_sem_approved": "Curricular units 2nd sem (approved)",
    "curricular_units_2nd_sem_grade": "Curricular units 2nd sem (grade)",
    "curricular_units_1st_sem_approved": "Curricular units 1st sem (approved)",
    "curricular_units_1st_sem_grade": "Curricular units 1st sem (grade)",
    "tuition_fees_up_to_date": "Tuition fees up to date",
    "scholarship_holder": "Scholarship holder",
    "age_at_enrollment": "Age at enrollment",
    "debtor": "Debtor",
    "gender": "Gender",
    "application_mode": "Application mode",
    "curricular_units_2nd_sem_evaluations": "Curricular units 2nd sem (evaluations)",
    "curricular_units_2nd_sem_enrolled": "Curricular units 2nd sem (enrolled)",
    "curricular_units_1st_sem_enrolled": "Curricular units 1st sem (enrolled)",
    "curricular_units_1st_sem_evaluations": "Curricular units 1st sem (evaluations)",
    "admission_grade": "Admission grade",
    "displaced": "Displaced",
    "previous_qualification_grade": "Previous qualification (grade)",
    "curricular_units_2nd_sem_without_evaluations": "Curricular units 2nd sem (without evaluations)",
    "marital_status": "Marital status",
    "application_order": "Application order",
    "daytime_evening_attendance": "Daytime/evening attendance",
    "mothers_qualification": "Mother's qualification",
    "curricular_units_1st_sem_without_evaluations": "Curricular units 1st sem (without evaluations)",
    "curricular_units_2nd_sem_credited": "Curricular units 2nd sem (credited)",
    "mothers_occupation": "Mother's occupation",
    "fathers_occupation": "Father's occupation",
    "curricular_units_1st_sem_credited": "Curricular units 1st sem (credited)",
    "previous_qualification": "Previous qualification",
    "fathers_qualification": "Father's qualification"
}

def encode_input(raw_data: dict) -> pd.DataFrame:
    """
    Encode raw input data into a format suitable for model prediction.
    """
    encoded = {}
    for key, value in raw_data.items():
        model_key = alias_map.get(key, key)
        if model_key in feature_mapping:
            if value not in feature_mapping[model_key]:
                raise ValueError(f"Value '{value}' not in feature mapping for '{model_key}'")
            encoded[model_key] = feature_mapping[model_key][value]
        else:
            encoded[model_key] = value
    return pd.DataFrame([encoded])

def predict_student_status(raw_data: dict) -> tuple[str, float]:
    """
    Predict student academic status.
    """
    # Encode input data dengan mapping nama fitur yang benar
    encoded_df = encode_input(raw_data)

    # Load model dan scaler
    model = joblib.load('model/mlp_model.model')
    scaler = joblib.load('model/standard_scaler.model')

    # Pastikan kolom sesuai urutan fitur model (kalau perlu, bisa disesuaikan)
    # Contoh: encoded_df = encoded_df[expected_feature_order]

    # Skala input
    scaled_input = scaler.transform(encoded_df)

    # Prediksi dan ambil confidence
    prediction = model.predict(scaled_input)
    confidence = model.predict_proba(scaled_input).max()

    # Mapping label prediksi ke nama kelas
    label_map = {0: "Dropout", 1: "Enrolled", 2: "Graduate"}
    label = label_map[prediction[0]]

    return label, round(confidence, 3)
