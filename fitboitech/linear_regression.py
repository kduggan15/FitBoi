from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.metrics import mean_squared_error

bodyfat_df = pd.read_csv('Bodyfat.csv', index_col=0)
model = train_linear_regression(bodyfat_df,bodyfat_target)

def train_linear_regression(X, y):
    """Trains and test linear regression model and returns mean_squared_error of
    y_test and y_predicted. 
    ----------
    X_train : array-like, shape = [n_samples, n_features]
        n_samples the number of samples
        n_features the number of features for each sample.
        
    y_train : array-like, shape = [n_samples]
        n_sample target values.
        
    Return 
        (float) mean_squared_error of (y_test and y_prediction)

    
    """

    lr = LinearRegression()
    lr.fit(X, y)
    
    return lr
