import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data from the file day_aul
day_aul = pd.read_csv('all_data.csv')


# Streamlit App
st.title('Dashboard Analisis Pengguna Sepeda')

# Tabs
tabs = ["Visualisasi Jumlah Pengguna", "Analisis Jumlah Pengguna"]
current_tab = st.sidebar.radio("Pilih Tab", tabs)

if current_tab == tabs[0]:
    # Visualisasi Jumlah Pengguna
    st.subheader('Visualisasi Jumlah Pengguna Sepeda per weathersit')

    # Membuat plot line chart
    jumlah_pengguna_berdasar_weathersit = day_aul.groupby('weathersit')['cnt'].sum()
    if 4 not in jumlah_pengguna_berdasar_weathersit.index:
        jumlah_pengguna_berdasar_weathersit.loc[4] = 0
    # Menampilkan jumlah pengguna sepeda berdasarkan cuaca(weathersit)
    st.write("Jumlah pengguna sepeda berdasarkan weathersit:")
    st.write(jumlah_pengguna_berdasar_weathersit)
    # Visualisasi dengan bar plot
    fig, ax = plt.subplots()
    ax.bar(jumlah_pengguna_berdasar_weathersit.index, jumlah_pengguna_berdasar_weathersit)
    ax.set_xlabel('cuaca')
    ax.set_ylabel('Jumlah Pengguna Sepeda')
    ax.set_title('Jumlah Pengguna Sepeda per cuaca')
    # Menampilkan plot di Streamlit
    st.pyplot(fig)
elif current_tab == tabs[1]:
    # Analisis Jumlah Pengguna
    st.subheader('Analisis Jumlah Pengguna Sepeda per Bulan')

    # Menghitung jumlah pengguna sepeda per bulan
    jumlah_pengguna_per_mnth = day_aul.groupby('mnth')['cnt'].sum()

    # Menampilkan hasil perhitungan
    st.write("Jumlah pengguna sepeda per bulan:")
    st.write(jumlah_pengguna_per_mnth)

    # Visualisasi dengan bar plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(jumlah_pengguna_per_mnth.index, jumlah_pengguna_per_mnth)
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Jumlah Pengguna Sepeda')
    ax.set_title('Jumlah Pengguna Sepeda per Bulan')

    # Menampilkan plot di aplikasi Streamlit
    st.pyplot(fig)
