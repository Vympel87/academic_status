# client/components/result_display.py

import streamlit as st

def display_result(result: dict):
	st.subheader("📄 Hasil Prediksi")
	if "error" in result:
		st.error(f"Terjadi kesalahan: {result['error']}")
	elif "status" in result:
		if result["status"] == "Lulus":
			st.success("✅ Mahasiswa dinyatakan **Lulus**.")
		else:
			st.warning("⚠️ Mahasiswa **Tidak Lulus**.")
	else:
		st.info("Belum ada hasil yang ditampilkan.")
