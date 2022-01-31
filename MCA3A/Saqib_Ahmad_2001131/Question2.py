# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 11:01:22 2022

@author: Saqib Ahmad
"""
# train-test split evaluation random forest on the housing dataset
import pandas as pd
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
# load dataset
dataframe = pd.read_csv("pollution.csv")
data = dataframe.values
# split into inputs and outputs
X, y = data[:, :-1], data[:, -1]
print(X.shape, y.shape)
# split into train test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=1)
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)
