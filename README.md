# Frozen-Soil-Dielectric-constant-model
A frozen soil dielectric constant model was constructed based on datasets and typical machine learning algorithms. These models have huge advantages to retrieve crucial surface soil properties.
##Introduction
The build soil dielectric constant model can be used in an border application conditions. 
Specifically, the operating frequency range is 0.2–20 GHz, 
the soil moisture content range is 0.05–0.4 m³/m³, 
and the soil salinity content range is 0–100 g/kg,

These soil dielectric constant models were built based on Random Forest algorithm through theoptimal model value, which was proven has the high-accuracy to simulating the soil dielectric properties,

##The model materials introduction

Datasets: contains a sample dataset that can be used to verify whether the model works properly.
EXample: contains sample data and example Python scripts for the soil dielectric constant real-part model.
Forward_models: includes predictive models for the real and imaginary parts of the soil dielectric constant, along with corresponding example Python scripts for their use.
SM_Retrieval_Model: contains soil moisture content predictive models for various scenarios, along with corresponding example Python scripts for their use.
Ssc_Retrieval_Model: contains soil salinity content predictive models for various scenarios, along with corresponding example Python scripts for their use.
The Basic_python_package: contains the required Python package files requirements.txt file with exact dependency versions.

The underlying foundational environment
windows 10
python==3.11

The required base packages and recommended versions
joblib 1.2.0
numpy 1.26.4
pandas 2.1.4
sklearn 1.2.2
matplotlib 3.8.0

Model Naming Convention:
Models in the Forward_models directory are for predicting the real (Real_model) and imaginary (Imaginary_model) parts of the soil dielectric constant.

For Retrieval models (e.g., SMRetrieval_Cband_Real), the name follows this structure:

Prefix (Target Variable): SM stands for Soil Moisture content; Ssc stands for Soil Salinity Content.

Condition/Parameters: Cband indicates the model is only applicable to C-band data; Real indicates that the input required is the real part of the dielectric constant.

Model Selection Guidance:
Choose a model based on your target variable and the data available in your application. Note that model accuracy may vary with different datasets. 
For specific performance details, please refer to the relevant publications.

Methods and Steps for Using the Models

Download the required models based on your research objectives and available data.
Load the models by referring to the corresponding example codes and proceed to achieve your goals.
There are two ways to use the models:
One is to compile the properties of the samples to be predicted into a separate file for batch prediction of the real and imaginary parts of the dielectric constant, 
as well as for retrieving soil moisture or salinity from the dielectric constant (corresponding to # Multi-Sample Batch Prediction for Soil Properties in the example code).
The other is to individually predict the properties of a single soil sample by inputting the sample attributes into the script to predict the real and imaginary parts of the dielectric constant and retrieve soil moisture or salinity from the dielectric constant (corresponding to #Single-Soil-Sample Prediction in the example code).
