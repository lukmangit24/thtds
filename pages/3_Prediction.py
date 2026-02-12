import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Prediksi Waktu Pengiriman", layout="wide")

st.title("🔮 Prediksi Waktu Pengiriman")

# ================= LOAD MODEL =================
@st.cache_resource
def load_model():
    return joblib.load("model/linear_model_pipeline.pkl")

model = load_model()

# ================= CARD HEADER =================
st.markdown("""
<div style="background-color:#1f2937;padding:20px;border-radius:15px;">
<h3 style="color:white;">📝 Masukkan Detail Pengiriman</h3>
<p style="color:#d1d5db;">Isi data berikut untuk memprediksi waktu pengiriman.</p>
</div>
""", unsafe_allow_html=True)

st.write("")

# ================= INPUT SECTION =================
col1, col2 = st.columns(2)

with col1:
    courier_exp = st.number_input(
        "Pengalaman Kurir (tahun)", 
        min_value=0.0, 
        max_value=20.0, 
        value=3.0
    )
    
    prep_time = st.number_input(
        "Waktu Persiapan (menit)", 
        min_value=1, 
        max_value=120, 
        value=20
    )
    
    distance = st.number_input(
        "Jarak Pengiriman (km)", 
        min_value=0.1, 
        max_value=50.0, 
        value=5.0
    )

with col2:
    weather = st.selectbox(
        "Kondisi Cuaca",
        ["Sunny", "Cloudy", "Rainy", "Stormy"]
    )
    
    traffic = st.selectbox(
        "Tingkat Kemacetan",
        ["Low", "Medium", "High"]
    )
    
    time_of_day = st.selectbox(
        "Waktu Pengiriman",
        ["Morning", "Afternoon", "Evening", "Night"]
    )
    
    vehicle_type = st.selectbox(
        "Jenis Kendaraan",
        ["Bike", "Car", "Scooter"]
    )

# ================= PREDICTION =================
if st.button("🚀 Prediksi Sekarang"):
    
    input_df = pd.DataFrame([{
        "Distance_km": distance,
        "Preparation_Time_min": prep_time,
        "Courier_Experience_yrs": courier_exp,
        "Weather": weather,
        "Traffic_Level": traffic,
        "Time_of_Day": time_of_day,
        "Vehicle_Type": vehicle_type
    }])
    
    try:
        prediction = model.predict(input_df)[0]
        
        st.markdown(f"""
        <div style="background-color:#111827;padding:30px;border-radius:20px;text-align:center;">
            <h2 style="color:white;">⏱ Estimasi Waktu Pengiriman</h2>
            <h1 style="color:#FF6B35;font-size:48px;">{prediction:.2f} menit</h1>
        </div>
        """, unsafe_allow_html=True)
        
    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")
