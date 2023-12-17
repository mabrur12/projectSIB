import streamlit as st
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
import os

pickle_in = open(os.getcwd() + "/models/xgboosts.pkl", "rb")
calculator = pickle.load(pickle_in)


def prediction(
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
):
    if DayOfWeek == "minggu":
        DayOfWeek = 1
    elif DayOfWeek == "senin":
        DayOfWeek = 2
    elif DayOfWeek == "selasa":
        DayOfWeek = 3
    elif DayOfWeek == "rabu":
        DayOfWeek = 4
    elif DayOfWeek == "kamis":
        DayOfWeek = 5
    elif DayOfWeek == "jum'at":
        DayOfWeek = 6
    else:
        DayOfWeek = 7

    if StoreType == "a":
        StoreType = 1
    elif StoreType == "b":
        StoreType = 2
    elif StoreType == "c":
        StoreType = 3
    else:
        StoreType = 4

    if Assortment == "a":
        Assortment = 0
    elif Assortment == "b":
        Assortment = 1
    else:
        Assortment = 2

    Promo = 1 if Promo == "ya" else 0
    SchoolHoliday = 1 if SchoolHoliday == "ya" else 0
    StateHoliday = 1 if StateHoliday == "ya" else 0
    Promo2 = 1 if Promo2 == "ya" else 0
    Promo2SinceWeek = 1 if Promo2SinceWeek == "ya" else 0
    PromoInterval_0 = 1 if PromoInterval_0 == "ya" else 0
    PromoInterval_Feb_May_Aug_Nov = 1 if PromoInterval_Feb_May_Aug_Nov == "ya" else 0
    PromoInterval_Jan_Apr_Jul_Oct = 1 if PromoInterval_Jan_Apr_Jul_Oct == "ya" else 0
    PromoInterval_Mar_Jun_Sept_Dec = 1 if PromoInterval_Mar_Jun_Sept_Dec == "ya" else 0

    # Making predictions
    prediction = calculator.predict(
        [
            [
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
            ]
        ]
    )

    return prediction


def visualize_feature_importance():
    # Gantilah dengan dataset atau fitur yang sesuai dengan model Anda
    # Contoh menggunakan feature_importances_ dari model RandomForest
    feature_importance = calculator.feature_importances_
    feature_names = [
        "DayOfWeek",
        "Customers",
        "Open",
        "Promo",
        "StateHoliday",
        "SchoolHoliday",
        "StoreType",
        "Assortment",
        "CompetitionDistance",
        "CompetitionOpenSinceMonth",
        "CompetitionOpenSinceYear",
        "Promo2",
        "Promo2SinceWeek",
        "PromoInterval_0",
        "PromoInterval_Feb,May,Aug,Nov",
        "PromoInterval_Jan,Apr,Jul,Oct",
        "PromoInterval_Mar,Jun,Sept,Dec",
    ]  # Gantilah dengan nama fitur sesuai dataset Anda

    # Visualisasi menggunakan bar plot
    # fig, ax = plt.subplots()
    st.set_option("deprecation.showPyplotGlobalUse", False)
    plt.figure(figsize=(8, 6))
    sns.barplot(x=feature_importance, y=feature_names)
    plt.title("Fitur Penting")
    plt.xlabel("Skor Fitur Penting")
    plt.ylabel("Fitur")
    st.pyplot()
