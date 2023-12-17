import pandas as pd
import os
import warnings


def read_data(path):
    return pd.read_csv(path)


def load_data():
    warnings.filterwarnings("ignore")
    current_directory = os.getcwd()
    sales_df = read_data(current_directory + "/datasets/rossmann-stores-data.csv")
    store_df = read_data(current_directory + "/datasets/store.csv")
    #  TODO: lclean data
    # clean data set

    # mengisi nilai yang null dengan 0
    store_df["CompetitionDistance"] = store_df["CompetitionDistance"].fillna(0)
    store_df["CompetitionOpenSinceMonth"] = store_df[
        "CompetitionOpenSinceMonth"
    ].fillna(0)
    store_df["CompetitionOpenSinceYear"] = store_df["CompetitionOpenSinceYear"].fillna(
        0
    )
    store_df["Promo2SinceWeek"] = store_df["Promo2SinceWeek"].fillna(0)
    store_df["Promo2SinceYear"] = store_df["Promo2SinceYear"].fillna(0)
    store_df["PromoInterval"] = store_df["PromoInterval"].fillna(0)

    final1 = pd.merge(sales_df, store_df, on="Store", how="left")
    # Change data types object to int
    final1.loc[final1["StateHoliday"] == "0", "StateHoliday"] = 0
    final1.loc[final1["StateHoliday"] == "a", "StateHoliday"] = 1
    final1.loc[final1["StateHoliday"] == "b", "StateHoliday"] = 2
    final1.loc[final1["StateHoliday"] == "c", "StateHoliday"] = 3
    # store the value with same column name i.e StateHoliday with function astype
    final1["StateHoliday"] = final1["StateHoliday"].astype(int, copy=False)

    # change Data Types object into int
    final1.loc[final1["Assortment"] == "a", "Assortment"] = 0
    final1.loc[final1["Assortment"] == "b", "Assortment"] = 1
    final1.loc[final1["Assortment"] == "c", "Assortment"] = 2
    # store the value with same column name i.e Assortment with function astype
    final1["Assortment"] = final1["Assortment"].astype(int, copy=False)

    # change Data Types object into int
    final1.loc[final1["StoreType"] == "a", "StoreType"] = 0
    final1.loc[final1["StoreType"] == "b", "StoreType"] = 1
    final1.loc[final1["StoreType"] == "c", "StoreType"] = 2
    final1.loc[final1["StoreType"] == "d", "StoreType"] = 3
    # store the value with same column name i.e Assortment with function astype
    final1["StoreType"] = final1["StoreType"].astype(int, copy=False)

    # code for changing format of date from object to datetime
    final1["Date"] = pd.to_datetime(final1["Date"], format="%Y-%m-%d")

    # code for change object into date format
    final1["CompetitionOpenSinceMonth"] = pd.DatetimeIndex(final1["Date"]).month
    # code for change float into integer
    final1["CompetitionOpenSinceYear"] = final1["CompetitionOpenSinceYear"].astype(int)
    final1["Promo2SinceYear"] = final1["Promo2SinceYear"].astype(int)

    # code for change float into integer
    final1["CompetitionDistance"] = final1["CompetitionDistance"].astype(int)
    final1["Promo2SinceWeek"] = final1["Promo2SinceWeek"].astype(int)

    final1.to_csv(current_directory + "/datasets/merge_data/cleandata.csv", index=False)

    return final1
