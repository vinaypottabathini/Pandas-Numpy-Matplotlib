#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 13:04:29 2023

@author: vinay
"""

# Importing the Required Packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import os


# Getting the Excel File Paths from Datasets to Read
assign_folder_path = os.path.dirname(os.path.dirname(os.getcwd()))
ExcelTestData1_path = assign_folder_path+'/Assignment_Data_&_References/Example_Data_V2/ExcelTestData1.xlsx'

#Reading the ExcelTestData1.xlsx File
excel_file_1 = pd.read_excel(ExcelTestData1_path, sheet_name='Sheet1')


#Exclude the Units Row (ft, us/ft, g/cc) and made into Numpy Array
sheet_data = np.array(excel_file_1)[1:] 


# Histogram for Whole Data with 3 Columns(MD, DT1, RHOB1) in ExcelTestData1.xlsx file
colors = ["blue", "orange", "green"]
fig, ax = plt.subplots()
ax.set_title('Histogram of Excel Test Data 1')


# Assigning Colors and Labels for legends
handles = [Rectangle((0, 0), 1, 1, color=c, ec="k") for c in colors]
labels = ['MD(ft)', 'DT1(us/ft)', 'RHOB1(g/cc)']
ax.legend(handles, labels)


#Showing the Histogram Figure
ax.hist(sheet_data) 


# Extracting Column B DT1(us/ft) from Sheet
B_column = list(excel_file_1['DT1'])[1:]

# Histogram for Column B- DT1 in 3 Columns(MD, DT1, RHOB1) in ExcelTestData1.xlsx file
colors = ["orange"]
fig2, ax2 = plt.subplots()
ax2.set_title('Histogram for Column B DT1(us/ft)')

# Assigning Colors and Labels for legends
handles = [Rectangle((0, 0), 1, 1, color=c, ec="k") for c in colors]
labels = [ 'DT1(us/ft)']
ax2.legend(handles, labels)

#Showing the Histogram Figure
ax2.hist(B_column, color='orange')