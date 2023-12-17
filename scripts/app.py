from preproccessing.app import load_data
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import xgboost as xgb
import pandas as pd
import numpy as np
import os
import pickle
import mlflow
import mlflow.sklearn
from mlflow import log_metric, log_param, log_artifacts
import matplotlib.pyplot as plt

# Import packages for logging
import logging
import logging.handlers


def load_logging():
    handler = logging.handlers.WatchedFileHandler(
        os.environ.get("LOGFILE", os.getcwd() + "/logs/mlflow.log")
    )
    formatter = logging.Formatter(logging.BASIC_FORMAT)
    handler.setFormatter(formatter)
    root = logging.getLogger()
    root.setLevel(os.environ.get("LOGLEVEL", "INFO"))
    root.addHandler(handler)
    logging.info("Testing Loggings")


def train_test_csv(final1, target, prediktor):
    data = final1.copy()
    # Create the data of independent variables
    U = data[prediktor].values
    # Create the dependent variable data
    V = data[target].values
    print("Separating Training Dataset", U)
    try:
        U_train, U_test, v_train, v_test = train_test_split(
            U, V, test_size=0.2, random_state=0
        )

    except Exception as e:
        print(e)
        logging.debug(
            f"Exception occured in separating dataset into x & y_training dataset, {e}"
        )

    try:
        U_train_csv = pd.DataFrame(U_train)
        U_train_csv.to_csv(os.getcwd() + "/datasets/train_data/X_train.csv")

        v_train_csv = pd.DataFrame(v_train)
        v_train_csv.to_csv(os.getcwd() + "/datasets/train_data/y_train.csv")

        U_test_csv = pd.DataFrame(U_test)
        U_test_csv.to_csv(os.getcwd() + "/datasets/test_data/X_test.csv")

        v_test_csv = pd.DataFrame(v_test)
        v_test_csv.to_csv(os.getcwd() + "/datasets/test_data/y_train.csv")
        logging.info(f"Separate dataset to save successfully")
    except Exception as e:
        logging.debug(
            f"Exception occured in save separating dataset into x & y_training dataset, {e}"
        )

    return U_train, U_test, v_train, v_test


def xgboost_fit(U_train, U_test, v_train, v_test):
    xgboost = xgb.XGBRegressor(n_estimators=500, max_depth=8, n_jobs=2)
    xgboost.fit(U_train, v_train)
    v_pred_xgb = xgboost.predict(U_test)
    mlflow.sklearn.log_model(xgboost, "model")

    plt.hist(v_pred_xgb)

    MSE = mean_squared_error(v_test, v_pred_xgb)
    print("MSE :", MSE)

    RMSE = np.sqrt(MSE)
    print("RMSE :", RMSE)

    sales_mean = np.mean(v_test)
    RMPSE = RMSE / sales_mean
    print("RMPSE :", RMPSE)

    r2 = r2_score(v_test, v_pred_xgb)
    print("R2 :", r2)
    return xgboost


def save_model(model):
    pickle.dump(model, open(os.getcwd() + "/models/xgboost.pkl", "wb"))

    print("SAVED: model with algoritma xgboost")


def rmspe(y, y_pred):
    rmspe = np.sqrt(np.mean((y - y_pred) ** 2))
    return rmspe


def main():
    mlflow.set_experiment(experiment_name="Exp01-Xgboost")
    print("Loading logging, and Dataset")
    load_logging()

    final = load_data()
    final1 = pd.get_dummies(final, columns=["PromoInterval"])

    # defining dependent variable
    dep_var = "Sales"

    # defining independent variable
    indep_var = final1.columns.drop(["Store", "Promo2SinceYear", "Date", "Sales"])

    U_train, U_test, v_train, v_test = train_test_csv(final1, dep_var, indep_var)
    log_param("Size of X train set", U_train.shape)
    log_param("Size of X test set", U_test.shape)
    log_param("Size of y train set", v_train.shape)
    log_param("Size of y test set", v_test.shape)
    logging.info(f"separating dataset into x & y_training dataset successfully")
    xgboost = xgboost_fit(U_train, U_test, v_train, v_test)
    # save_model(xgboost)

    Y_pred = xgboost.predict(U_test)
    error = rmspe(v_test, Y_pred)
    # evaluating the model
    print(error)
    print("Error associated with our Model is: %.3f " % error)

    log_metric("Error Associated with the Model is", error)

    print("Model saved in run %s" % mlflow.active_run().info.run_uuid)
    log_artifacts(os.getcwd() + "/scripts/outputs")


if __name__ == "__main__":
    main()
