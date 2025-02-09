from timeit import default_timer as timer
from sklearn import metrics
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import os
import requests
import warnings

warnings.filterwarnings("ignore")

# Load data file (will get cached after first download)

dataset_dir = "data"
dataset_name = "year_prediction_msd"
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00203/YearPredictionMSD.txt.zip"

os.makedirs(dataset_dir, exist_ok=True)
local_url = os.path.join(dataset_dir, os.path.basename(url))

if not os.path.isfile(local_url):
    response = requests.get(url, stream=True)
    with open(local_url, "wb+") as file:
        for data in response.iter_content(8192):
            file.write(data)

# Load CSV file into x, y

year = pd.read_csv(local_url, header=None)
x = year.iloc[:, 1:].to_numpy(dtype=np.float32)
y = year.iloc[:, 0].to_numpy(dtype=np.float32)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=0)
x_train.shape, x_test.shape, y_train.shape, y_test.shape

# Normalise the dataset

from sklearn.preprocessing import MinMaxScaler, StandardScaler

scaler_x = MinMaxScaler()
scaler_y = StandardScaler()

scaler_x.fit(x_train)
x_train = scaler_x.transform(x_train)
x_test = scaler_x.transform(x_test)

scaler_y.fit(y_train.reshape(-1, 1))
y_train = scaler_y.transform(y_train.reshape(-1, 1)).ravel()
y_test = scaler_y.transform(y_test.reshape(-1, 1)).ravel()

# Add GPU support

from sklearnex import patch_sklearn

patch_sklearn()

# Find line of best fit

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_validate

params = {"n_jobs": -1, "copy_X": False}
start = timer()
model = LinearRegression(**params).fit(x_train, y_train)
train_patched = timer() - start

# Forecast values of y

y_predict = model.predict(x_test)
mse_metric_opt = metrics.mean_squared_error(y_test, y_predict)
print(f"GPU Scikit-learn MSE: {mse_metric_opt} in {train_patched}s")

# Cross validate

scores = cross_validate(model, x_train, y_train, cv=10)
post_validation = timer() - train_patched
print(f"Scores {scores} in {post_validation}s")