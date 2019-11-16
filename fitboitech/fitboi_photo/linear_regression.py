from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.metrics import mean_squared_error

def train_linear_regression(X, y):

    lr = LinearRegression()
    lr.fit(X, y)

    return lr

def predictBF(neck, waist):
    X = np.array([neck, waist]).reshape(1,-1)
    y = model.predict(X)
    return y

bodyfat_df = pd.read_csv('Bodyfat.csv', index_col=0)
bodyfat_target = bodyfat_df.bodyfat
bodyfat_df = bodyfat_df[['Neck','Abdomen']]
model = train_linear_regression(bodyfat_df,bodyfat_target)
print(predictBF(25,90))
