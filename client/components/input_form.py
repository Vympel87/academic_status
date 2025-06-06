# client/components/input_form.py

import streamlit as st

# Salin feature_mapping dari server/util/feature_mapping.py (hanya key dan list stringnya)
feature_mapping = {
    "Marital status": [
        "single",
        "married",
        "widower",
        "divorced",
        "facto union",
        "legally separated",
    ],
    "Application mode": [
        "1st phase - general contingent",
        "Ordinance No. 612/93",
        "1st phase - special contingent (Azores Island)",
        "Holders of other higher courses",
        "Ordinance No. 854-B/99",
        "International student (bachelor)",
        "1st phase - special contingent (Madeira Island)",
        "2nd phase - general contingent",
        "3rd phase - general contingent",
        "Ordinance No. 533-A/99, item b2) (Different Plan)",
        "Ordinance No. 533-A/99, item b3 (Other Institution)",
        "Over 23 years old",
        "Transfer",
        "Change of course",
        "Technological specialization diploma holders",
        "Change of institution/course",
        "Short cycle diploma holders",
        "Change of institution/course (International)",
    ],
    "Daytime/evening attendance": ["daytime", "evening"],
    "Previous qualification": [
        "Secondary education",
        "Higher education - bachelor's degree",
        "Higher education - degree",
        "Higher education - master's",
        "Higher education - doctorate",
        "Frequency of higher education",
        "12th year of schooling - not completed",
        "11th year of schooling - not completed",
        "Other - 11th year of schooling",
        "10th year of schooling",
        "10th year of schooling - not completed",
        "Basic education 3rd cycle (9th/10th/11th year)",
        "Basic education 2nd cycle (6th/7th/8th year)",
        "Technological specialization course",
        "Higher education - degree (1st cycle)",
        "Professional higher technical course",
        "Higher education - master (2nd cycle)",
    ],
    "Mother's qualification": [
        "Secondary Education - 12th Year of Schooling or Eq.",
        "Higher Education - Bachelor's Degree",
        "Higher Education - Degree",
        "Higher Education - Master's",
        "Higher Education - Doctorate",
        "Frequency of Higher Education",
        "12th Year of Schooling - Not Completed",
        "11th Year of Schooling - Not Completed",
        "7th Year (Old)",
        "Other - 11th Year of Schooling",
        "10th Year of Schooling",
        "General commerce course",
        "Basic Education 3rd Cycle (9th/10th/11th Year)",
        "Technical-professional course",
        "7th year of schooling",
        "2nd cycle of the general high school course",
        "9th Year of Schooling - Not Completed",
        "8th year of schooling",
        "Unknown",
        "Can't read or write",
        "Can read without having a 4th year of schooling",
        "Basic education 1st cycle (4th/5th year)",
        "Basic Education 2nd Cycle (6th/7th/8th Year)",
        "Technological specialization course",
        "Higher education - degree (1st cycle)",
        "Specialized higher studies course",
        "Professional higher technical course",
        "Higher Education - Master (2nd cycle)",
        "Higher Education - Doctorate (3rd cycle)",
    ],
    "Father's qualification": [
        "Secondary Education - 12th Year of Schooling or Eq.",
        "Higher Education - Bachelor's Degree",
        "Higher Education - Degree",
        "Higher Education - Master's",
        "Higher Education - Doctorate",
        "Frequency of Higher Education",
        "12th Year of Schooling - Not Completed",
        "11th Year of Schooling - Not Completed",
        "7th Year (Old)",
        "Other - 11th Year of Schooling",
        "2nd year complementary high school course",
        "10th Year of Schooling",
        "General commerce course",
        "Basic Education 3rd Cycle (9th/10th/11th Year)",
        "Complementary High School Course",
        "Technical-professional course",
        "Complementary High School Course - not concluded",
        "7th year of schooling",
        "2nd cycle of the general high school course",
        "9th Year of Schooling - Not Completed",
        "8th year of schooling",
        "General Course of Administration and Commerce",
        "Supplementary Accounting and Administration",
        "Unknown",
        "Can't read or write",
        "Can read without having a 4th year of schooling",
        "Basic education 1st cycle (4th/5th year)",
        "Basic Education 2nd Cycle (6th/7th/8th Year)",
        "Technological specialization course",
        "Higher education - degree (1st cycle)",
        "Specialized higher studies course",
        "Professional higher technical course",
        "Higher Education - Master (2nd cycle)",
        "Higher Education - Doctorate (3rd cycle)",
    ],
    "Mother's occupation": [
        "Student",
        "Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers",
        "Specialists in Intellectual and Scientific Activities",
        "Intermediate Level Technicians and Professions",
        "Administrative staff",
        "Personal Services, Security and Safety Workers and Sellers",
        "Farmers and Skilled Workers in Agriculture, Fisheries and Forestry",
        "Skilled Workers in Industry, Construction and Craftsmen",
        "Installation and Machine Operators and Assembly Workers",
        "Unskilled Workers",
        "Armed Forces Professions",
        "Other Situation",
        "(blank)",
    ],
    "Father's occupation": [
        "Student",
        "Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers",
        "Specialists in Intellectual and Scientific Activities",
        "Intermediate Level Technicians and Professions",
        "Administrative staff",
        "Personal Services, Security and Safety Workers and Sellers",
        "Farmers and Skilled Workers in Agriculture, Fisheries and Forestry",
        "Skilled Workers in Industry, Construction and Craftsmen",
        "Installation and Machine Operators and Assembly Workers",
        "Unskilled Workers",
        "Armed Forces Professions",
        "Other Situation",
        "(blank)",
    ],
    "Displaced": ["yes", "no"],
    "Debtor": ["yes", "no"],
    "Tuition fees up to date": ["yes", "no"],
    "Gender": ["male", "female"],
    "Scholarship holder": ["yes", "no"],
}


def input_form():
    st.subheader("📝 Input Form")

    name = st.text_input("Student Name", placeholder="Cristiano ronaldo")
    age = st.number_input("Age at Enrollemnt", min_value=15, max_value=100, value=18)
    gender = st.selectbox("Gender", feature_mapping["Gender"])
    marital_status = st.selectbox(
        "Marital Status", feature_mapping["Marital status"]
    )
    displaced = st.radio("Is Student Displayed? (Merantau)", feature_mapping["Displaced"])
    daytime_evening = st.selectbox(
        "Time of Attendance", feature_mapping["Daytime/evening attendance"]
    )
    scholarship = st.radio("Is Student a Scholarship Holder?", feature_mapping["Scholarship holder"])
    debtor = st.radio("Is Student a Debtor?", feature_mapping["Debtor"])
    tuition_fees = st.radio(
        "Tuition Fees Up To Date? (Apakah Membayar UKT Lunas?)", feature_mapping["Tuition fees up to date"]
    )
    application_mode = st.selectbox("Application Mode (Jalur Masuk)", feature_mapping["Application mode"])
    application_order = st.number_input(
        "Application Order (Urutan Pendaftaran)", min_value=1, max_value=20, value=1
    )
    admission_grade = st.number_input(
        "Admission Grade (Nilai Seleksi Masuk)", min_value=0.0, max_value=20.0, value=14.5
    )
    previous_qualification = st.selectbox(
        "Previous Qualification", feature_mapping["Previous qualification"]
    )
    previous_qualification_grade = st.number_input(
        "Previous Qualification Grade", min_value=0.0, max_value=20.0, value=15.0
    )
    mother_qualification = st.selectbox(
        "Mother's Qualification", feature_mapping["Mother's qualification"]
    )
    mother_occupation = st.selectbox(
        "Mother's Occupation", feature_mapping["Mother's occupation"]
    )
    father_qualification = st.selectbox(
        "Father's Qualification", feature_mapping["Father's qualification"]
    )
    father_occupation = st.selectbox(
        "Father's Occupation", feature_mapping["Father's occupation"]
    )

    # Data akademik
    cu_1st_approved = st.number_input(
        "Jumlah Unit Kurikulum 1st Sem (Lulus)", min_value=0, max_value=100, value=0
    )
    cu_1st_grade = st.number_input(
        "Nilai Unit Kurikulum 1st Sem", min_value=0.0, max_value=20.0, value=0.0
    )
    cu_1st_enrolled = st.number_input(
        "Jumlah Unit Kurikulum 1st Sem (Diambil)", min_value=0, max_value=100, value=0
    )
    cu_1st_evaluations = st.number_input(
        "Evaluasi Jumlah Unit Kurikulum 1st Sem", min_value=0, max_value=100, value=0
    )
    cu_1st_credited = st.number_input(
        "Jumlah Unit Kurikulum 1st Sem (Diakui)", min_value=0, max_value=100, value=0
    )
    cu_1st_without_eval = st.number_input(
        "Jumlah Unit Kurikulum 1st Sem (Tanpa Evaluasi)", min_value=0, max_value=100, value=0
    )

    cu_2nd_approved = st.number_input(
        "Jumlah Unit Kurikulum 2nd Sem (Lulus)", min_value=0, max_value=100, value=0
    )
    cu_2nd_grade = st.number_input(
        "Nilai Unit Kurikulum 2nd Sem", min_value=0.0, max_value=20.0, value=0.0
    )
    cu_2nd_enrolled = st.number_input(
        "Jumlah Unit Kurikulum 2nd Sem (Diambil)", min_value=0, max_value=100, value=0
    )
    cu_2nd_evaluations = st.number_input(
        "Evaluasi Jumlah Unit Kurikulum 2nd Sem", min_value=0, max_value=100, value=0
    )
    cu_2nd_credited = st.number_input(
        "Jumlah Unit Kurikulum 2nd Sem (Diakui)", min_value=0, max_value=100, value=0
    )
    cu_2nd_without_eval = st.number_input(
        "Jumlah Unit Kurikulum 2nd Sem (Tanpa Evaluasi)", min_value=0, max_value=100, value=0
    )

    submit = st.button("🔍 Prediksi Status Akademik")

    data = {
        "name": name,
        "Age at enrollment": age,
        "Gender": gender,
        "Marital status": marital_status,
        "Displaced": displaced,
        "Daytime/evening attendance": daytime_evening,
        "Scholarship holder": scholarship,
        "Debtor": debtor,
        "Tuition fees up to date": tuition_fees,
        "Application mode": application_mode,
        "Application order": application_order,
        "Admission grade": admission_grade,
        "Previous qualification": previous_qualification,
        "Previous qualification (grade)": previous_qualification_grade,
        "Mother's qualification": mother_qualification,
        "Mother's occupation": mother_occupation,
        "Father's qualification": father_qualification,
        "Father's occupation": father_occupation,
        "Curricular units 1st sem (approved)": cu_1st_approved,
        "Curricular units 1st sem (grade)": cu_1st_grade,
        "Curricular units 1st sem (enrolled)": cu_1st_enrolled,
        "Curricular units 1st sem (evaluations)": cu_1st_evaluations,
        "Curricular units 1st sem (credited)": cu_1st_credited,
        "Curricular units 1st sem (without evaluations)": cu_1st_without_eval,
        "Curricular units 2nd sem (approved)": cu_2nd_approved,
        "Curricular units 2nd sem (grade)": cu_2nd_grade,
        "Curricular units 2nd sem (enrolled)": cu_2nd_enrolled,
        "Curricular units 2nd sem (evaluations)": cu_2nd_evaluations,
        "Curricular units 2nd sem (credited)": cu_2nd_credited,
        "Curricular units 2nd sem (without evaluations)": cu_2nd_without_eval,
    }

    return submit, data
