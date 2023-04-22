#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 23:40:54 2023

@author: gridlex
"""

# Importing the Required Packages
import pandas as pd
import numpy as np
import h5py
import os


# Getting the ExcelTestData1.xlsx File Path from Example_Data_V2 to Read
assign_folder_path = os.path.dirname(os.path.dirname(os.getcwd()))
ExcelTestData1_path = assign_folder_path+'/Assignment_Data_&_References/Example_Data_V2/ExcelTestData1.xlsx'

# Reading the ExcelTestData1.xlsx file using pandas read_csv
excel_file_1_data = pd.read_excel(ExcelTestData1_path, sheet_name='Sheet1')[1:]

# Converting the data to float to keep it Compatible to the HDF file dataset we are about create
excel_file_1_data.astype(float)




# Creating HDF File named test1.hdf using h5py
file = h5py.File("test1.hdf", "w")

# Creating Dataset named 'EXCEL_SHEET_DATA' in test1.hdf file with float datatype and shape same as excel_file_1_data and Writing excel_file_1_data into Dataset
dataset = file.create_dataset("EXCEL_SHEET_DATA", data=excel_file_1_data ,shape=excel_file_1_data.shape, dtype=np.float64)

#Closing the File
file.close()


# Again Reading the File test1.hdf using h5py and printing to check the data has been updated or not 
read = h5py.File('test1.hdf', 'r')
dset = read['EXCEL_SHEET_DATA']
print(dset)