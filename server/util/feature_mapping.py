feature_mapping = {
        "Marital status": {
            "single": 1, "married": 2, "widower": 3, "divorced": 4,
            "facto union": 5, "legally separated": 6
        },
        "Application mode": {
            "1st phase - general contingent": 1,
            "Ordinance No. 612/93": 2,
            "1st phase - special contingent (Azores Island)": 5,
            "Holders of other higher courses": 7,
            "Ordinance No. 854-B/99": 10,
            "International student (bachelor)": 15,
            "1st phase - special contingent (Madeira Island)": 16,
            "2nd phase - general contingent": 17,
            "3rd phase - general contingent": 18,
            "Ordinance No. 533-A/99, item b2) (Different Plan)": 26,
            "Ordinance No. 533-A/99, item b3 (Other Institution)": 27,
            "Over 23 years old": 39,
            "Transfer": 42,
            "Change of course": 43,
            "Technological specialization diploma holders": 44,
            "Change of institution/course": 51,
            "Short cycle diploma holders": 53,
            "Change of institution/course (International)": 57
        },
        "Daytime/evening attendance": {
            "daytime": 1, "evening": 0
        },
        "Previous qualification": {
            "Secondary education": 1,
            "Higher education - bachelor's degree": 2,
            "Higher education - degree": 3,
            "Higher education - master's": 4,
            "Higher education - doctorate": 5,
            "Frequency of higher education": 6,
            "12th year of schooling - not completed": 9,
            "11th year of schooling - not completed": 10,
            "Other - 11th year of schooling": 12,
            "10th year of schooling": 14,
            "10th year of schooling - not completed": 15,
            "Basic education 3rd cycle (9th/10th/11th year)": 19,
            "Basic education 2nd cycle (6th/7th/8th year)": 38,
            "Technological specialization course": 39,
            "Higher education - degree (1st cycle)": 40,
            "Professional higher technical course": 42,
            "Higher education - master (2nd cycle)": 43
        },
        "Mother's qualification": {
            "Secondary Education - 12th Year of Schooling or Eq.": 1,
            "Higher Education - Bachelor's Degree": 2,
            "Higher Education - Degree": 3,
            "Higher Education - Master's": 4,
            "Higher Education - Doctorate": 5,
            "Frequency of Higher Education": 6,
            "12th Year of Schooling - Not Completed": 9,
            "11th Year of Schooling - Not Completed": 10,
            "7th Year (Old)": 11,
            "Other - 11th Year of Schooling": 12,
            "10th Year of Schooling": 14,
            "General commerce course": 18,
            "Basic Education 3rd Cycle (9th/10th/11th Year)": 19,
            "Technical-professional course": 22,
            "7th year of schooling": 26,
            "2nd cycle of the general high school course": 27,
            "9th Year of Schooling - Not Completed": 29,
            "8th year of schooling": 30,
            "Unknown": 34,
            "Can't read or write": 35,
            "Can read without having a 4th year of schooling": 36,
            "Basic education 1st cycle (4th/5th year)": 37,
            "Basic Education 2nd Cycle (6th/7th/8th Year)": 38,
            "Technological specialization course": 39,
            "Higher education - degree (1st cycle)": 40,
            "Specialized higher studies course": 41,
            "Professional higher technical course": 42,
            "Higher Education - Master (2nd cycle)": 43,
            "Higher Education - Doctorate (3rd cycle)": 44
        },
        "Father's qualification": {
            "Secondary Education - 12th Year of Schooling or Eq.": 1,
            "Higher Education - Bachelor's Degree": 2,
            "Higher Education - Degree": 3,
            "Higher Education - Master's": 4,
            "Higher Education - Doctorate": 5,
            "Frequency of Higher Education": 6,
            "12th Year of Schooling - Not Completed": 9,
            "11th Year of Schooling - Not Completed": 10,
            "7th Year (Old)": 11,
            "Other - 11th Year of Schooling": 12,
            "2nd year complementary high school course": 13,
            "10th Year of Schooling": 14,
            "General commerce course": 18,
            "Basic Education 3rd Cycle (9th/10th/11th Year)": 19,
            "Complementary High School Course": 20,
            "Technical-professional course": 22,
            "Complementary High School Course - not concluded": 25,
            "7th year of schooling": 26,
            "2nd cycle of the general high school course": 27,
            "9th Year of Schooling - Not Completed": 29,
            "8th year of schooling": 30,
            "General Course of Administration and Commerce": 31,
            "Supplementary Accounting and Administration": 33,
            "Unknown": 34,
            "Can't read or write": 35,
            "Can read without having a 4th year of schooling": 36,
            "Basic education 1st cycle (4th/5th year)": 37,
            "Basic Education 2nd Cycle (6th/7th/8th Year)": 38,
            "Technological specialization course": 39,
            "Higher education - degree (1st cycle)": 40,
            "Specialized higher studies course": 41,
            "Professional higher technical course": 42,
            "Higher Education - Master (2nd cycle)": 43,
            "Higher Education - Doctorate (3rd cycle)": 44
        },
        "Mother's occupation": {
            "Student": 0,
            "Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers": 1,
            "Specialists in Intellectual and Scientific Activities": 2,
            "Intermediate Level Technicians and Professions": 3,
            "Administrative staff": 4,
            "Personal Services, Security and Safety Workers and Sellers": 5,
            "Farmers and Skilled Workers in Agriculture, Fisheries and Forestry": 6,
            "Skilled Workers in Industry, Construction and Craftsmen": 7,
            "Installation and Machine Operators and Assembly Workers": 8,
            "Unskilled Workers": 9,
            "Armed Forces Professions": 10,
            "Other Situation": 90,
            "(blank)": 99
        },
        "Father's occupation": {
            "Student": 0,
            "Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers": 1,
            "Specialists in Intellectual and Scientific Activities": 2,
            "Intermediate Level Technicians and Professions": 3,
            "Administrative staff": 4,
            "Personal Services, Security and Safety Workers and Sellers": 5,
            "Farmers and Skilled Workers in Agriculture, Fisheries and Forestry": 6,
            "Skilled Workers in Industry, Construction and Craftsmen": 7,
            "Installation and Machine Operators and Assembly Workers": 8,
            "Unskilled Workers": 9,
            "Armed Forces Professions": 10,
            "Other Situation": 90,
            "(blank)": 99
        },
        "Displaced": {"yes": 1, "no": 0},
        "Debtor": {"yes": 1, "no": 0},
        "Tuition fees up to date": {"yes": 1, "no": 0},
        "Gender": {"male": 1, "female": 0},
        "Scholarship holder": {"yes": 1, "no": 0}
    }
