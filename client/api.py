# client/api.py

import requests

# CLASSIFY_API_URL = "http://127.0.0.1:8000/api/ml/classify"
CLASSIFY_API_URL = "https://academicstatus-production.up.railway.app/api/ml/classify"

def predict_status(input_data: dict):
    try:
        # mengambil data name langsung dari input_data
        name = input_data.get("name", "Unknown Student")

        response = requests.post(CLASSIFY_API_URL, json=input_data)
        response.raise_for_status()
        result = response.json()
        # Mengembalikan status dan confidence jika response sesuai format
        if result.get("status") == "success" and "data" in result:
            return {
                "name": name,
                "status": result["data"].get("status"),
                "confidence": result["data"].get("confidence")
            }
        else:
            return {"error": "Invalid response format"}
        # return {"status": "Lulus" if input_data["nilai_akhir"] > 60 and input_data["kehadiran"] > 75 else "Tidak Lulus"}
    except requests.RequestException as e:
        return {"error": str(e)}
