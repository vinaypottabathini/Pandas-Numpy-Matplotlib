#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 00:04:58 2023

@author: vinay
"""

# Importing the Required Packages
import os
import h5py
import time
import numpy as np


# HDF5_USE_FILE_LOCKING is made False in os.environ as it is locking to open (may be we can't open this file concurrently or it's process not terminated)
os.environ["HDF5_USE_FILE_LOCKING"] = "FALSE"


# Taking the time before reading the test1.hdf file
start_time = time.time()

# Reading the test1.hdf file Using h5py
read = h5py.File('test1.hdf', 'r')
dset = read['EXCEL_SHEET_DATA']



# Taking the No of Columns in Dataset through Shape
no_of_columns = dset.shape[1]


# Taking Each Column Data from Dataset and Saving into new files with Naming Convention 'column_{column_number}.txt'
for col_num in range(no_of_columns):
    col_data = np.array(dset[:, col_num])
    output_col_file = f'column_{col_num}.txt'
    np.savetxt(output_col_file, col_data, delimiter=',')
    
# Taking the time after creating output files
end_time = time.time()

# Calculating time taken for Reading the test1.hdf and writing each column into output files
print(end_time-start_time, 'Seconds')