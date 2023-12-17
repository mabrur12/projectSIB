import streamlit as st
from actions.app import *
import math


st.set_page_config(page_title="Dashboard", layout="wide")
st.markdown(
    "<h1 style='color:#0b4eab;font-size:36px;border-radius:10px;'>Dashboard | Retail Sales Prediction Model </h1>",
    unsafe_allow_html=True,
)

def main():
    html_temp = """ 
    
    """

    st.markdown(html_temp, unsafe_allow_html=True)

    # Sidebar dengan input pengguna
    menu = st.sidebar.radio("Menu", ["Prediksi", "Visualisasi Fitur Penting"])

    if menu == "Prediksi":
        DayOfWeek = st.selectbox(
            "Masukkan Hari",
            ("senin", "selasa", "rabu", "kamis", "jum'at", "sabtu", "minggu"),
        )
        Customers = st.number_input("Jumlah pelanggan")
        StoreType = st.selectbox("pilih tipe toko", ("a", "b", "c", "d"))
        Promo = st.selectbox("apakah kamu dalam promo ?", ("ya", "tidak"))
        StateHoliday = st.selectbox("Apakah libur nasional ?", ("ya", "tidak"))
        SchoolHoliday = st.selectbox("Apakah libur sekolah ?", ("ya", "tidak"))
        Assortment = st.selectbox("Pilih jenis", ("a", "b", "c"))
        CompetitionDistance = st.number_input("Masukan jarak kompetisi")
        CompetitionOpenSinceMonth = st.number_input(
            "Masukan jarak kompetisi baru bulan ini"
        )
        CompetitionOpenSinceYear = st.number_input(
            "Masukan jarak kompetisi baru tahun ini"
        )
        Promo2 = st.selectbox("Apakah ada promo ke dua ?", ("ya", "tidak"))
        Promo2SinceWeek = st.selectbox(
            "Apakah kamu ada didalam promo minggu ini", ("ya", "tidak")
        )
        result = ""
        Open = 1
        PromoInterval_0 = st.selectbox("Apakah ada interval promo ?", ("ya", "tidak"))
        PromoInterval_Feb_May_Aug_Nov = st.selectbox(
            "Apakah ada interval promo di bulan ini (Feb, May, Aug, Nov) ?",
            ("ya", "tidak"),
        )
        PromoInterval_Jan_Apr_Jul_Oct = st.selectbox(
            "Apakah ada interval promo di bulan ini (Jan, Apr, Jul, Oct)?",
            ("ya", "tidak"),
        )
        PromoInterval_Mar_Jun_Sept_Dec = st.selectbox(
            "Apakah ada interval promo di bulan ini (Mar, Jun, Sept, Dec)?",
            ("ya", "tidak"),
        )

        if st.button("Predict"):
            result = prediction(
                DayOfWeek,
                Customers,
                Open,
                Promo,
                StateHoliday,
                SchoolHoliday,
                StoreType,
                Assortment,
                CompetitionDistance,
                CompetitionOpenSinceMonth,
                CompetitionOpenSinceYear,
                Promo2,
                Promo2SinceWeek,
                PromoInterval_0,
                PromoInterval_Feb_May_Aug_Nov,
                PromoInterval_Jan_Apr_Jul_Oct,
                PromoInterval_Mar_Jun_Sept_Dec,
            )
            st.success("Perkiraan terjual adalah {}".format(math.ceil(result[0])))
    else:
        visualize_feature_importance()


if __name__ == "__main__":
    main()
