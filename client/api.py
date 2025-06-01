# client/api.py

import requests

API_URL = "http://localhost:8000/predict"  # Ganti dengan URL endpoint yang sebenarnya

def predict_status(input_data: dict):
    # Dummy return kalau API belum tersedia
    # Gantilah blok try-except ini dengan actual request nanti
    try:
        # Sementara dummy response untuk simulasi
        return {"status": "Lulus" if input_data["nilai_akhir"] > 60 and input_data["kehadiran"] > 75 else "Tidak Lulus"}
        # Uncomment ini saat backend sudah siap
        # response = requests.post(API_URL, json=input_data)
        # response.raise_for_status()
        # return response.json()
    except requests.RequestException as e:
        return {"error": str(e)}
