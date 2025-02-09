from timeit import default_timer as timer
from sklearn import metrics
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import os
import requests
import warnings
import dpctl

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

# Add GPU support

from sklearnex import patch_sklearn, config_context

patch_sklearn()

# Find line of best fit

from sklearn.cluster import DBSCAN

start = timer()
with config_context(target_offload="gpu:0"):
   clustering = DBSCAN(eps=3, min_samples=2).fit(x)
train_patched = timer() - start

print(f"GPU Scikit-learn MSE: {train_patched}")
