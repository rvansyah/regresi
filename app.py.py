import streamlit as st
import pandas as pd
import numpy as np
import joblib  # Sesuaikan jika Anda pakai pickle atau cara lain

# Load model Anda di sini (ganti dengan path dan metode load yang sesuai)
# model = joblib.load('model_income.pkl')

st.title("Prediksi Income Berdasarkan Age & Experience")

st.write("Masukkan data baru untuk memprediksi Income:")

# Input dari user
new_age = st.number_input("Masukkan nilai Age (Usia):", min_value=0.0, max_value=150.0, value=25.0)
new_experience = st.number_input("Masukkan nilai Experience (Pengalaman):", min_value=0.0, max_value=100.0, value=1.0)

predict_button = st.button("Prediksi Income")

if predict_button:
    try:
        # Buat DataFrame dari input baru dengan nama kolom yang sama seperti saat training
        new_data_df = pd.DataFrame([[new_age, new_experience]], columns=['Age', 'Experience'])

        # Lakukan prediksi menggunakan model yang sudah dilatih
        predicted_income = model.predict(new_data_df)  # predicted_income harus array 2D atau 1D

        st.success(f"Untuk Age = {new_age} dan Experience = {new_experience}:")
        st.info(f"Prediksi Income adalah: ${predicted_income[0][0]:,.2f}")

    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")