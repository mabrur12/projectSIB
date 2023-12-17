# Retail Sales prediction across multiple stores

**Project Type**    - EDA/Regression/Classification/Unsupervised

- This dataset is a live dataset of Rossmann Stores. On analsysing this problem we observe that Rossmann problem is a regression problem and our primarily goal is to predict the sales figures of Rossmann problem. In this Notebook we work on following topics

Analysing the Dataset by using Exploratory Data Analysis. Using Exponential Moving Averages analyse Trends and Seasonality in Roseman dataset. Analyse Regression analysis using following prediction analysis, A. Linear Regression Analysis B. Elastic Regression ( Lasso and Ridge Regression). C. Random Forest Regression. d.adaboost and Xgboost.

By applying above algorthim we find accuracy of 98% by Xgboost

## Part 02. Procces Retail Sales Prediction Multiple Store

- Data Preprocessing,
- Building models with sklearn pipelines,
- Choosing a loss function,
- Post Prediction analysis,
- Serialize models,
- Building model with deep learning, and
- Using MLFlow to serve the prediction

### This part is done in directory /notebooks 'Retail Sales Predication-ML project .ipynb'

## Part 03. Tutorial setup to run this project

### CLONE REPOSITORY

```bash
$ git clone <remote_repo> (ex: git clone https://github.com/perdanaph/Pharmaceutical-Sales-Prediction)
# clone github repository 
```

### HOW TO SETTING VENV PYTHON

```bash
$ python -m venv <yourenvname> (ex: myenv)
$ ./<yourenvname>/Scripts/activate (ex: ./myenv/Scripts/activate)
# setting venv in your local computer
```

### HOW TO INSTALL DEPENDENCIES

- before this step, make sure your venv activated
- for example

```powershell
(env) C:\User\<Name>\directory\..\streamlit-project>
```

#### Install dependencies in file requirements.txt

```bash
$ pip install -r requirements.txt
# install all dependencies
```

#### Run MLflow

- this step will building a model ML using **xgboost** algorithm
- to run this step you can add command in the terminal

```bash
$ python scripts/app.py
# running MLflow to build model
```

## Part 04. RUNNING THE STREAMLIT

- to run streamlit you can add the terminal command like this

```bash
$ streamlit run app.py
# run the streamlit
```
