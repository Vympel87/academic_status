# client/app.py

import streamlit as st
from components.input_form import input_form
from components.result_display import display_result
from api import predict_status

def main():
    st.set_page_config(page_title="Dashboard Status Akademik", layout="centered")

    st.title("📊 Dashboard Klasifikasi Status Akademik")
    st.markdown("Masukkan data mahasiswa untuk memprediksi status akademik berdasarkan nilai dan kehadiran.")

    submit, input_data = input_form()

    if submit:
        result = predict_status(input_data)
        display_result(result)

if __name__ == "__main__":
    main()
