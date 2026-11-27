# -*- coding: utf-8 -*-
"""
Created on Mon Dec  1 21:06:09 2025

@author: Liang Gao
"""

#download the model with pkl as local lication
import joblib   
import numpy as np  
import pandas as pd 
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
############################################################################################################
## The introduction of model input parameters 
# Real:      The Real part of soil dielectric constant
# Imaginary: The Imaginary part of soil dielectric constant
# Frequency: Microwave frequency (0.01 - 16 GHz)
# Temperature:Soil temperature(-30°C - 0°C)
# matter:    Organic matter(%)
# rou_s:     Soil specific dendity(g/cm³)  
# rou_b:     Soil bulk dendity(g/cm³)  
#
##The introduction of model output parameters 
# Ice: the predicted Soil ice content

############################################################################################################
# Multi-Sample Batch Prediction for Soil Properties
##Load the saved model  
# this is an example about soil ice content model
# model_input_path is the address of the data storage folder
model_input_path = r'...\modelxg_temprealimagmatterpredicted_Ice.plk'
model_Xgboost = joblib.load(model_input_path)

#Load the example dataset
# input_path_file is the address of the data storage folder
input_path_file = r'...\sample.csv'
data = pd.read_csv(input_path_file)
keys = data.keys()
data = data.dropna()

data['frequency'] = data['frequency']/1000000000
# choose the model parameters
X = data[['Real', 'Imaginary',  'frequency', 'matter', 'Temperature', 'rou', 'rou_b',]]
# choose the model prediction parameters
yy = data['Ice']  
X_test = X
y_test = yy
#split example dataset as the train-samples and test-samples
# X_train, X_test, y_train, y_test = train_test_split(X, yy, test_size=0.7, random_state=42)
# predict the real part of soil dielectric constant 
y_predict = model_Xgboost.predict(X_test)
#
plt.figure(figsize=(7, 5), dpi=300)
plt.scatter(y_test, y_predict)
plt.xlabel('The True Ice Content (m³/m³)')
plt.ylabel('The Predicted Ice Content (m³/m³)')
plt.show()

############################################################################################################
#Single-Soil-Sample Prediction
##built the input variables X_test
X = {'Real':[16.9], 'Imaginary':[16.9],'frequency':[5.5],'matter': [0.46], 'Temperature':[-10], 'rou':[2.65], 'rou_b':[1.35]}

X = pd.DataFrame(X)
y_predict = model_Xgboost.predict(X)

