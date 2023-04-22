#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 04:06:36 2023

@author: vinay
"""


# Importing the Required Packages
import pandas as pd
import numpy as np
import h5py
import os
import matplotlib.pyplot as plt


# HDF5_USE_FILE_LOCKING is made False in os.environ as it is locking to open (may be we can't open this file concurrently or it's process not terminated)
os.environ["HDF5_USE_FILE_LOCKING"] = "FALSE"



assign_folder_path = os.path.dirname(os.path.dirname(os.getcwd()))
file_path = assign_folder_path+'/Assignment_Data_&_References/Example_Data_V2/HDF_Data/Test.petrabytes'
petrabytes_file = h5py.File(file_path, 'r')

# Printing the List of Groups Available in Petrabytes File
list(petrabytes_file.keys())


# Taking the Well 1 Data from psa_data Group and well_1 Dataset
well1 = list(petrabytes_file['psa_data']['well_1']['1234'])

# Taking the Well 2 Data from psa_data Group and well_2 Dataset
well2 = list(petrabytes_file['psa_data']['well_2']['2222'])


# Labeling x-axis and y-axis with 'Well 1 Data' and 'Well 2 Data' respectively
plt.xlabel('Well 1 Data')
plt.ylabel('Well 2 Data')

# Naming Plot Title as 'Petrabytes Well 1 - Well 2 Plot'
plt.title('Petrabytes Well 1 - Well 2 Plot')

#Showing the Figure
plt.plot(well1, well2)
plt.show()