import streamlit as st

# =============================
# KONFIGURASI HALAMAN
# =============================
st.set_page_config(
    page_title="Prediksi Waktu Pengiriman Makanan",
    layout="wide"
)

# =============================
# GLOBAL STYLE (UI MODERN)
# =============================
st.markdown("""
<style>
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

h1 {
    color: #FF6B35;
    font-weight: 800;
}

h2, h3 {
    color: #2E3A59;
}

.card {
    background-color: #1E1E1E;
    padding: 22px;
    border-radius: 16px;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.35);
    margin-bottom: 20px;
}

.metric {
    font-size: 28px;
    font-weight: bold;
    color: #FF6B35;
}

.stButton>button {
    background-color: #FF6B35;
    color: white;
    border-radius: 12px;
    padding: 12px 24px;
    font-weight: 700;
}
</style>
""", unsafe_allow_html=True)

# =============================
# HEADER
# =============================
st.title("🚚 Prediksi Waktu Pengiriman Makanan")

st.markdown("""
<div class="card">
<p>
Aplikasi ini memprediksi <b>waktu pengiriman makanan (menit)</b> menggunakan
model <b>Machine Learning</b> berdasarkan karakteristik pesanan, kondisi lalu lintas,
dan faktor operasional lainnya.
</p>
</div>
""", unsafe_allow_html=True)

# =============================
# PROJECT BACKGROUND
# =============================
st.header("📌 Project Background")

st.markdown("""
Dalam industri food delivery yang kompetitif, estimasi waktu pengiriman yang akurat
menjadi faktor krusial dalam meningkatkan kepuasan pelanggan dan efisiensi operasional.

Dataset yang digunakan berasal dari <b>Food Delivery Time Prediction (Kaggle)</b>,
yang berisi informasi terkait jarak pengiriman, waktu persiapan, pengalaman kurir,
kondisi cuaca, tingkat kemacetan, waktu pengiriman, dan jenis kendaraan.

Dengan memanfaatkan Machine Learning, proyek ini bertujuan untuk membantu
perusahaan memperkirakan waktu pengiriman secara lebih akurat dan berbasis data.
""")

# =============================
# PROBLEM STATEMENT
# =============================
st.header("❗ Problem Statement")

st.markdown("""
Perusahaan menghadapi tantangan dalam:
- Estimasi waktu pengiriman yang sering meleset
- Ketidakpuasan pelanggan akibat keterlambatan
- Kurangnya sistem prediksi berbasis data

Tanpa sistem prediksi yang akurat, operasional menjadi kurang optimal
dan customer experience dapat menurun.
""")

# =============================
# OBJECTIVE
# =============================
st.header("🎯 Project Objective")

st.markdown("""
Tujuan dari proyek ini adalah:

1. Membangun model Machine Learning untuk memprediksi waktu pengiriman (regression).
2. Mengidentifikasi faktor-faktor utama yang mempengaruhi lamanya pengiriman.
3. Mengukur performa model menggunakan metrik evaluasi yang relevan.
4. Mengembangkan aplikasi interaktif berbasis Streamlit untuk simulasi prediksi.
""")

# =============================
# MODEL & METRICS
# =============================
st.header("🤖 Model & Evaluation Metrics")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
        <h3>Model yang Digunakan</h3>
        <ul>
            <li>Linear Regression (Baseline & Final Model)</li>
            <li>Ridge Regression</li>
            <li>Decision Tree Regressor</li>
        </ul>
        <p>
        Model terbaik yang dipilih adalah <b>Linear Regression + Scaling</b>
        karena memberikan performa paling stabil dan interpretatif.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h3>Evaluation Metrics</h3>
        <ul>
            <li><b>MAE</b> (Mean Absolute Error)</li>
            <li><b>RMSE</b> (Root Mean Squared Error)</li>
            <li><b>MAPE</b> (Mean Absolute Percentage Error)</li>
        </ul>
        <p>
        MAE digunakan untuk mengukur rata-rata kesalahan absolut,
        RMSE untuk menghukum error besar,
        dan MAPE untuk melihat persentase error terhadap nilai aktual.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.info("Gunakan menu di sidebar untuk menjelajahi EDA, Modeling, dan halaman Prediction 👈")
