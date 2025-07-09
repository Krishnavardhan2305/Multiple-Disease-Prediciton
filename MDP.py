import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load models
diabetes_model = pickle.load(open('diabetes_trained_model.sav', 'rb'))
breastcancer_model = pickle.load(open('BreastCancer_trained_model.sav', 'rb'))

# Sidebar menu
with st.sidebar:
    selected = option_menu(
        menu_title="Multiple Disease Predictor",
        options=["Diabetes", "Breast_Cancer"],
        icons=["activity", "capsule"],
        default_index=0
    )

# ==================== Diabetes Page ====================
if selected == 'Diabetes':
    st.title('Diabetes Prediction using ML')
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the Person')

    diab_diagnosis = ''

    if st.button('Diabetes Test Result'):
        try:
            diab_prediction = diabetes_model.predict(
                [[float(Pregnancies), float(Glucose), float(BloodPressure), float(SkinThickness),
                  float(Insulin), float(BMI), float(DiabetesPedigreeFunction), float(Age)]]
            )

            if diab_prediction[0] == 1:
                diab_diagnosis = 'The person is diabetic'
            else:
                diab_diagnosis = 'The person is not diabetic'
        except:
            diab_diagnosis = "⚠️ Please enter valid numeric values."

    st.success(diab_diagnosis)

# ==================== Breast Cancer Page ====================
if selected == "Breast_Cancer":
    st.title('Breast Cancer Prediction using ML')

    # Display inputs in 5 columns for better layout
    col1, col2, col3, col4, col5 = st.columns(5)

    # Input fields based on your dataset (first 30 features)
    with col1:
        mean_radius = st.text_input('mean radius')
        mean_smoothness = st.text_input('mean smoothness')
        texture_error = st.text_input('texture error')
        smoothness_error = st.text_input('smoothness error')
        worst_radius = st.text_input('worst radius')
        worst_smoothness = st.text_input('worst smoothness')

    with col2:
        mean_texture = st.text_input('mean texture')
        mean_compactness = st.text_input('mean compactness')
        perimeter_error = st.text_input('perimeter error')
        compactness_error = st.text_input('compactness error')
        worst_texture = st.text_input('worst texture')
        worst_compactness = st.text_input('worst compactness')

    with col3:
        mean_perimeter = st.text_input('mean perimeter')
        mean_concavity = st.text_input('mean concavity')
        area_error = st.text_input('area error')
        concavity_error = st.text_input('concavity error')
        worst_perimeter = st.text_input('worst perimeter')
        worst_concavity = st.text_input('worst concavity')

    with col4:
        mean_area = st.text_input('mean area')
        mean_concave_points = st.text_input('mean concave points')
        concave_points_error = st.text_input('concave points error')
        symmetry_error = st.text_input('symmetry error')
        worst_area = st.text_input('worst area')
        worst_concave_points = st.text_input('worst concave points')

    with col5:
        mean_symmetry = st.text_input('mean symmetry')
        mean_fractal_dimension = st.text_input('mean fractal dimension')
        fractal_dimension_error = st.text_input('fractal dimension error')
        worst_fractal_dimension = st.text_input('worst fractal dimension')
        worst_symmetry = st.text_input('worst symmetry')

    cancer_diagnosis = ''

    if st.button('Breast Cancer Test Result'):
        try:
            input_data = [
                float(mean_radius), float(mean_texture), float(mean_perimeter), float(mean_area), float(mean_smoothness),
                float(mean_compactness), float(mean_concavity), float(mean_concave_points), float(mean_symmetry), float(mean_fractal_dimension),
                float(radius_error := 0),  # optional: fill in missing values
                float(texture_error), float(perimeter_error), float(area_error), float(smoothness_error),
                float(compactness_error), float(concavity_error), float(concave_points_error), float(symmetry_error), float(fractal_dimension_error),
                float(worst_radius), float(worst_texture), float(worst_perimeter), float(worst_area), float(worst_smoothness),
                float(worst_compactness), float(worst_concavity), float(worst_concave_points), float(worst_symmetry), float(worst_fractal_dimension)
            ]

            cancer_prediction = breastcancer_model.predict([input_data])

            if cancer_prediction[0] == 1:
                cancer_diagnosis = 'The person has breast cancer'
            else:
                cancer_diagnosis = 'The person does not have breast cancer'
        except:
            cancer_diagnosis = "⚠️ Please enter all required numeric values."

    st.success(cancer_diagnosis)
