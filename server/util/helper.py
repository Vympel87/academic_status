from server.util.feature_mapping import feature_mapping
import pandas as pd
import joblib


def encode_input(raw_data: dict) -> pd.DataFrame:
    """
    Encode raw input data into a format suitable for model prediction.

    Parameters:
    -----------
    raw_data : dict
        A dictionary containing raw student data input where some fields
        require categorical mapping (e.g., gender, application mode).

    Returns:
    --------
    pd.DataFrame
        A single-row DataFrame with encoded and ordered values ready for scaling and prediction.
    """
    encoded = {}
    for key, value in raw_data.items():
        if key in feature_mapping:
            encoded[key] = feature_mapping[key][value]
        else:
            encoded[key] = value

    return pd.DataFrame([encoded])


def predict_student_status(raw_data: dict) -> tuple[str, float]:
    """
    Predict the academic status of a student (Dropout, Enrolled, or Graduate) 
    based on the input features.

    Parameters:
    -----------
    raw_data : dict
        A dictionary of user input with human-readable categorical values.

    Returns:
    --------
    tuple[str, float]
        A tuple containing:
        - the predicted student status label (str),
        - the model's confidence score (float, 3 decimal places).
    """
    # Encode the raw input
    encoded_df = encode_input(raw_data)

    # Load model and scaler
    model = joblib.load('server/model/mlp_model.model')
    scaler = joblib.load('server/model/standard_scaler.model')

    # Scale the encoded input
    scaled_input = scaler.transform(encoded_df)

    # Predict label and confidence
    prediction = model.predict(scaled_input)
    confidence = model.predict_proba(scaled_input).max()

    # Map label index to descriptive label
    label_map = {0: "Dropout", 1: "Enrolled", 2: "Graduate"}
    label = label_map[prediction[0]]

    return label, round(confidence, 3)
