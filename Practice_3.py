#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 16:49:00 2023

@author: vinay
"""

# Importing the required packages
import pandas as pd
import numpy as np
import h5py
import os

# Getting the File Path from Datasets to Read
assign_folder_path = os.path.dirname(os.path.dirname(os.getcwd()))
file_path = assign_folder_path+'/Assignment_Data_&_References/Datasets/Mud_Weight.csv'


# Reading the Mud_Weight.csv file using pandas read_csv
# Slicing the first row at 0 index to remove the units MD-'m' and Mud_Weight - 'lbm/galUS'
MD_Weight_Data = pd.read_csv(file_path, delimiter=',', usecols=['MD', 'Mud_Weight']).values[1:]

# Converting the data to respective types as they are in strings while we read
MD_Weight_Data[:, 0] = MD_Weight_Data[:, 0].astype(int)
MD_Weight_Data[:, 1] = MD_Weight_Data[:, 1].astype(float)


# Creating DataFrame with Updated Data
MD_Weight_df = pd.DataFrame(MD_Weight_Data, columns=['MD', 'Mud_Weight'])

# Multiplying the Mud_Weight Column values with 10
MD_Weight_df['Mud_Weight'] *= 10

#Saving the Updated Data to CSV File Mud_Weight_PI.csv
MD_Weight_df.to_csv('Mud_Weight_PI.csv', index=False)


# Getting the File Path of Mud_Weight_PI.csv from Current Directory to Read
mud_weight_pi_filepath = os.getcwd()+'/Mud_Weight_PI.csv'


# Reading the Mud_Weight_PI.csv file using pandas read_csv
# Slicing the first row at 0 index to remove the units MD(m) and Mud_Weight(lbm/galUS)
MD_Weight_PI_data = pd.read_csv(mud_weight_pi_filepath, delimiter=',', usecols=['MD', 'Mud_Weight']).values[1:]

# Converting the datatype of MD_Weight_PI_data- object to float as we are about to create HDF File Dataset 'DATA' whose datatype will be float
MD_Weight_PI_data.astype(float)


# Creating HDF File named MD_HEIGHT_AND_WEIGHT_HDF_FILE.h5
hdf = h5py.File("MD_HEIGHT_AND_WEIGHT_HDF_FILE.h5", "w")


# Creating Dataset named 'DATA' in HDF file with float datatype and shape same as MD_Weight_PI_data and writing the MD_Weight_PI_data into the DataSet
dataset = hdf.create_dataset("DATA", data=MD_Weight_PI_data ,shape=MD_Weight_PI_data.shape, dtype=np.float64)


# Creating Attributes 'X_Unit' and 'Y_Unit' with values 'm' and 'kg/m3'
dataset.attrs['X_Unit']='m'
dataset.attrs['Y_Unit']='kg/m3'


# Closing the hdf file MD_HEIGHT_AND_WEIGHT_HDF_FILE.h5
hdf.close()


# Reading the File MD_HEIGHT_AND_WEIGHT_HDF_FILE.h5 and printing to check the data has been updated or not
read = h5py.File('MD_HEIGHT_AND_WEIGHT_HDF_FILE.h5', 'r')
dset = read['DATA']
print(dset.attrs['X_Unit'])
print(dset.attrs['Y_Unit'])
print(dset)