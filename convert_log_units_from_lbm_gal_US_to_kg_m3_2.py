#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 16:38:59 2023

@author: vinay
"""

# Importing the required packages
import pandas as pd
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


## We have 1 lbm/galUS = 119.826427 kg/m3
## Multiplying with 119.826427 on Weight (index 1 in list of lists)
MD_Weight_Data[:, 1]*=119.826427


# Creating DataFrame with Updated Data
MD_Weight_df = pd.DataFrame(MD_Weight_Data, columns=['MD(m)', 'Mud_Weight(kg/m3)'])


# Creating a New File as Mud_Weight_Converted.csv
# Here index is False as we are not referring to include the row count column in output file.
MD_Weight_df.to_csv('Mud_Weight_Converted.csv', index=False) 
