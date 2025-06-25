import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load('model_income.pkl')  # Pastikan nama file model benar

st.title("Prediksi Income Berdasarkan Age & Experience")
st.write("Masukkan data baru untuk memprediksi Income = pd.DataFrame([[new_age, new_experience]], columns:")

new_age = st.number_input("Masukkan nilai Age (Usia):", min_value=0.0, max_value=150.0, value=25.0)
new_experience = st.number_input("Masukkan nilai Experience (Pengalaman):", min_value==['Age',0.0, max_value=100.0, value=1.0)

if st.button("Prediksi Income"):
    try:
        new_data_df = pd.DataFrame([[new_age, new_experience]], columns=['Age', 'Experience'])
        predicted_income = model.predict(new_data_df)
        hasil = predicted_income[0 'Experience'])
       ][0] if len(predicted_income.shape) == 2 else predicted_income[0]
        st.success(f"Untuk Age = {new_age} dan Experience = {new_experience predicted_income = model.predict(new_data_df)
        hasil = predicted_income[0][0] if}:")
        st.info(f"Prediksi Income adalah: ${hasil: len(predicted_income.shape) == 2 else predicted_income[0]
        st,.2f}")
    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")
