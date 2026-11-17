# -*- coding: utf-8 -*-
"""
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
# Ice:        ice content (0.005 - 0.6 m³/m³)
# Frequency:  Microwave frequency (0.01 - 16 GHz)
# Matter:     Soil content(0 - 1)
# Temperature:Soil temperature(-30°C - 0°C)
# rou:        Soil specific dendity 
# rou_b:      Soil bulk dendity 
#
##The introduction of model output parameters 
# real: the predicted real part of soil dielectric constant

############################################################################################################
# Multi-Sample Batch Prediction for Soil Properties
##Load the saved soil dielectric constant model  
# this is an example about soil dielectric constant real part prediction model
# model_input_path is the address of the data storage folder
model_input_path = r'...\Real_model.plk'
model = joblib.load(model_input_path)

#Load the example dataset
# input_path_file is the address of the data storage folder
input_path_file = r'...\sample.csv'
data = pd.read_csv(input_path_file)
keys = data.keys()
data = data.dropna()
data['frequency'] = data['frequency']/1000000000
# choose the model parameters
X = data[['Ice', 'frequency', 'Matter', 'Temperature', 'rou', 'rou_b']]
# choose the model prediction parameters
yy = data['real']  
#split example dataset as the train-samples and test-samples
X_train, X_test, y_train, y_test = train_test_split(X, yy, test_size=0.7, random_state=42)
# predict the real part of soil dielectric constant 
y_predict = model.predict(X_test)
#
plt.figure(figsize=(7, 5), dpi=300)
plt.scatter(y_test, y_predict)
plt.xlabel('The Predicted Real Part')
plt.ylabel('The Measured Real Part')
plt.show()

############################################################################################################
#Single-Soil-Sample Prediction
##built the input variables X_test
X = {'Ice':[0.2], 'frequency':[5.5],'Matter': [0.46], 'Temperature':[-15], 'rou':[2.65], 'rou_b':[1.35]}
if (X['frequency'][0] < 0.01) or ((X['frequency'][0] > 16)):
    print('This model is not applicable within this frequency range.')
if ((X['Temperature'][0] > 0) or (X['Temperature'][0] < -30)):
    print('This model is not applicable within this Temperature range.')
if ((X['Ice'][0] > 0.005) or (X['Ice'][0] < 0.6)):
    print('This model is not applicable within this ice range.')
X = pd.DataFrame(X)
y_predict = model.predict(X)


