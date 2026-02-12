import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="EDA", layout="wide")

st.title("📊 Exploratory Data Analysis")

# ================= LOAD DATA =================
@st.cache_data
def load_data():
    return pd.read_csv("data/Food_Delivery_Times.csv")

df = load_data()

# ================= METRIC =================
col1, col2, col3 = st.columns(3)

col1.metric("Total Data", df.shape[0])
col2.metric("Total Fitur", df.shape[1])
col3.metric("Missing Value", df.isna().sum().sum())

st.divider()

# ================= PREVIEW =================
st.subheader("📌 Preview Dataset")
st.dataframe(df.head())

st.divider()

# =====================================================
# DISTRIBUSI NUMERICAL FEATURES
# =====================================================
st.subheader("📈 Distribusi Fitur Numerik")

num_cols = [
    "Distance_km",
    "Preparation_Time_min",
    "Courier_Experience_yrs",
    "Delivery_Time_min"
]

selected_num = st.selectbox("Pilih fitur numerik:", num_cols)

fig, ax = plt.subplots()
df[selected_num].hist(bins=30, ax=ax)
ax.set_xlabel(selected_num)
ax.set_ylabel("Frekuensi")
st.pyplot(fig)

st.divider()

# =====================================================
# BOXPLOT UNTUK DETEKSI OUTLIER
# =====================================================
st.subheader("📦 Deteksi Outlier (Boxplot)")

selected_box = st.selectbox("Pilih fitur untuk boxplot:", num_cols)

fig2, ax2 = plt.subplots()
ax2.boxplot(df[selected_box], vert=False)
ax2.set_xlabel(selected_box)
st.pyplot(fig2)

st.divider()

# =====================================================
# ANALISIS KATEGORIKAL
# =====================================================
st.subheader("📊 Analisis Fitur Kategorikal")

cat_cols = [
    "Weather",
    "Traffic_Level",
    "Time_of_Day",
    "Vehicle_Type"
]

selected_cat = st.selectbox("Pilih fitur kategorikal:", cat_cols)

fig3, ax3 = plt.subplots()
df[selected_cat].value_counts().plot(kind="bar", ax=ax3)
ax3.set_ylabel("Jumlah")
st.pyplot(fig3)

st.divider()

# =====================================================
# HUBUNGAN FITUR DENGAN TARGET
# =====================================================
st.subheader("🔎 Hubungan Fitur dengan Waktu Pengiriman")

selected_relation = st.selectbox(
    "Pilih fitur numerik untuk dibandingkan dengan Delivery_Time_min:",
    ["Distance_km", "Preparation_Time_min", "Courier_Experience_yrs"]
)

fig4, ax4 = plt.subplots()
ax4.scatter(df[selected_relation], df["Delivery_Time_min"])
ax4.set_xlabel(selected_relation)
ax4.set_ylabel("Delivery_Time_min")
st.pyplot(fig4)

st.divider()

# =====================================================
# INSIGHT SECTION
# =====================================================
st.markdown("""
### 🔍 Insight Utama

- Distribusi waktu pengiriman cenderung **right-skewed**
- Jarak pengiriman memiliki korelasi positif terhadap waktu pengiriman
- Waktu persiapan juga meningkatkan total waktu delivery
- Traffic_Level berpengaruh signifikan terhadap lamanya pengiriman
- Jenis kendaraan mempengaruhi efisiensi waktu
""")
