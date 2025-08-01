import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ----- DATA LOADING AND PREPARATION -----
# Fungsi ini untuk menghindari loading ulang data setiap kali ada interaksi
@st.cache_data
def load_data():
    # Memuat data harian
    day_df = pd.read_csv("day.csv")
    
    # Mengubah tipe data tanggal
    day_df['dteday'] = pd.to_datetime(day_df['dteday'])
    
    # Mengganti angka dengan label yang lebih deskriptif
    day_df['season'] = day_df['season'].map({1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'})
    day_df['weathersit'] = day_df['weathersit'].map({1: 'Cerah', 2: 'Berkabut', 3: 'Hujan Ringan', 4: 'Hujan Lebat'})
    
    return day_df

# Memanggil fungsi untuk memuat data
day_df = load_data()


# ----- MAIN DASHBOARD -----
st.title('Dashboard Analisis Penyewaan Sepeda 🚲')

# Menampilkan kesimpulan utama
st.header('Kesimpulan Utama')

col1, col2 = st.columns(2)
with col1:
    st.metric(label="Kesimpulan Cuaca", value="Cerah")
with col2:
    st.metric(label="Kesimpulan Musim", value="Musim Gugur")

st.markdown("---")

# ----- VISUALISASI PERTANYAAN 1 -----
st.header('Bagaimana Pengaruh Cuaca Terhadap Jumlah Sewa?')

# Menyiapkan data untuk plot
weather_df = day_df.groupby("weathersit")["cnt"].mean().reset_index().sort_values("cnt", ascending=False)

# Membuat plot
fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.barplot(
    x="weathersit",
    y="cnt",
    data=weather_df,
    ax=ax1,
    palette="viridis"
)
ax1.set_title("Rata-Rata Penyewaan Sepeda Berdasarkan Kondisi Cuaca", fontsize=16, fontweight='bold')
ax1.set_xlabel("Kondisi Cuaca", fontsize=14, fontweight='bold')
ax1.set_ylabel("Rata-Rata Jumlah Sewa Harian", fontsize=14, fontweight='bold')
st.pyplot(fig1)

# ----- VISUALISASI PERTANYAAN 2 -----
st.header('Bagaimana Perbedaan Pola Sewa Berdasarkan Musim?')

# Menyiapkan data untuk plot
season_df = day_df.groupby("season")["cnt"].mean().reset_index().sort_values("cnt", ascending=False)

# Membuat plot
fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.barplot(
    x="season",
    y="cnt",
    data=season_df,
    ax=ax2,
    palette="plasma"
)
ax2.set_title("Rata-Rata Penyewaan Sepeda Berdasarkan Musim", fontsize=16, fontweight='bold')
ax2.set_xlabel("Musim", fontsize=14, fontweight='bold')
ax2.set_ylabel("Rata-Rata Jumlah Sewa Harian", fontsize=14, fontweight='bold')
st.pyplot(fig2)

st.caption('Copyright (c) Aditya Alfauzi 2025')