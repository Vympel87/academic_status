from util.feature_mapping import feature_mapping
import pandas as pd
import joblib

# Mapping dari snake_case ke nama alias sesuai model
alias_map = {
    "gpa": "Admission grade",
    "marital_status": "Marital status",
    "application_mode": "Application mode",
    "daytime_evening_attendance": "Daytime/evening attendance",
    "previous_qualification": "Previous qualification",
    "mothers_qualification": "Mother's qualification",
    "fathers_qualification": "Father's qualification",
    "mothers_occupation": "Mother's occupation",
    "fathers_occupation": "Father's occupation",
    "displaced": "Displaced",
    "debtor": "Debtor",
    "tuition_fees_up_to_date": "Tuition fees up to date",
    "gender": "Gender",
    "scholarship_holder": "Scholarship holder",
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
