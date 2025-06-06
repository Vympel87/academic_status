# client/components/result_display.py

import streamlit as st

def display_result(result: dict):
	st.subheader("📄 Prediction Status")
	if "error" in result:
		st.error(f"Terjadi kesalahan: {result['error']}")
	elif "status" in result:
		name = result["name"]
		status = result["status"]
		confidence = result.get("confidence", None)
		if status == "Graduate":
			st.success(f"✅ {name} dinyatakan **Lulus**.\n\nConfidence: {confidence:.2%}" if confidence is not None else "✅ {name} dinyatakan **Lulus**.")
		elif status == "Enrolled":
			st.info(f"ℹ️ {name} berstatus **Aktif/Terdaftar**.\n\nConfidence: {confidence:.2%}" if confidence is not None else "ℹ️ {name} berstatus **Aktif/Terdaftar**.")
		elif status == "Dropout":
			st.warning(f"⚠️ {name} **Dropout**.\n\nConfidence: {confidence:.2%}" if confidence is not None else "⚠️ {name} **Dropout**.")
		else:
			st.info(f"Status: {status}" + (f"\n\nConfidence: {confidence:.2%}" if confidence is not None else ""))
	else:
		st.info("Belum ada hasil yang ditampilkan.")
