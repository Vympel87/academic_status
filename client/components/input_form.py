# client/components/input_form.py

import streamlit as st

def input_form():
	st.subheader("📝 Formulir Input Mahasiswa")

	nama = st.text_input("Nama Mahasiswa")
	nilai_akhir = st.number_input("Nilai Akhir", min_value=0.0, max_value=100.0, step=0.1)
	kehadiran = st.number_input("Persentase Kehadiran (%)", min_value=0, max_value=100, step=1)

	submit = st.button("🔍 Prediksi Status Akademik")

	data = {
		"nama": nama,
		"nilai_akhir": nilai_akhir,
		"kehadiran": kehadiran,
	}

	return submit, data
