#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 03:08:16 2023

@author: vinay
"""

# Importing the Required Packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os



# Getting the Excel File Paths from Datasets to Read
assign_folder_path = os.path.dirname(os.path.dirname(os.getcwd()))
lat_and_long_data_file_path = assign_folder_path+'/Assignment_Data_&_References/Example_Data_V2/Latitude_Long_Example_Data.csv'

#Reading the Latitude_Long_Example_Data.csv File
lat_and_long_data = pd.read_csv(lat_and_long_data_file_path,  delimiter=',')



# Extracting Latitude Column Data
lat_data = np.array(lat_and_long_data['LAT'])



# Extracting Longitude Column Data
long_data = np.array(lat_and_long_data['LONG'])


# Plotting the Scatter Plot with latitude and Longitude Data
# plt.scatter will mark the matching points in the graph
plt.scatter(lat_data,long_data, color='red', marker='8')

# plt.plot will connect the points in the graph
plt.plot(lat_data, long_data, color='green')