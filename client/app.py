# client/app.py

import streamlit as st
from components.input_form import input_form
from components.result_display import display_result
from api import predict_status

def main():
    st.set_page_config(page_title="Dashboard Academic Status", layout="centered")

    st.title("📊 Classification Academic Status in Portugal")
    st.markdown("In this application, you can predict the academic status of students based on various features. Fill in the form below to get started.")

    submit, input_data = input_form()

    if submit:
        result = predict_status(input_data)
        display_result(result)

if __name__ == "__main__":
    main()
