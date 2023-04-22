#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 17:19:41 2023

@author: vinay
"""
# Importing the required packages
import pandas as pd
import numpy as np
import h5py
import os

# Getting the Survey_Data.csv File Path from Datasets to Read
assign_folder_path = os.path.dirname(os.path.dirname(os.getcwd()))
file_path = assign_folder_path+'/Assignment_Data_&_References/Datasets/Survey_Data.csv'


# Reading the Survey_Data.csv File
Survey_Data = pd.read_csv(file_path, delimiter=',')


# Getting and forming a dictionary as column_names to units for later use while Creating Attributes for Dataset
attributes = dict(zip(list(Survey_Data.columns), list(Survey_Data[:1].values[0])))


# Converting the data to float to keep it Compatible to the HDF file dataset we are about create
Survey_Data = Survey_Data[1:].astype(float)

# Checking datatype of all Columns are float or not 
print(Survey_Data.dtypes)


# Creating HDF File named Survey.h5
sf = h5py.File("Survey.h5", "w")

# Creating Dataset named 'DATA' in Survey.h5 file with float datatype and shape same as Survey_Data and Writing Survey_Data into Dataset
survey_dataset = sf.create_dataset("DATA", data=Survey_Data ,shape=Survey_Data.shape, dtype=np.float64)
    
#Printing and Checking Dataset
print(survey_dataset)

# Updating the Dataset 'DATA' with Attributes of the Survey Data 
survey_dataset.attrs.update({k: v for k, v in attributes.items()})

# Closing the Survey.h5 File
sf.close()

# Again Reading the File Survey.h5 and printing to check the data and Attributes has been updated or not 
read = h5py.File('Survey.h5', 'r')
dset = read['DATA']
print(dset.attrs)
print(dset.attrs['Azim'])
print(dset)