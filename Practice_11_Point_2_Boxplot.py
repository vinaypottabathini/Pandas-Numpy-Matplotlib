#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 12:35:07 2023

@author: gridlex
"""

# Importing the Required Packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


# Getting the Excel File Paths from Datasets to Read
assign_folder_path = os.path.dirname(os.path.dirname(os.getcwd()))
ExcelTestData1_path = assign_folder_path+'/Assignment_Data_&_References/Example_Data_V2/ExcelTestData1.xlsx'


#Reading the ExcelTestData1.xlsx File
excel_file_1 = pd.read_excel(ExcelTestData1_path, sheet_name='Sheet1')



## Box Plot for Whole Data in the Sheet (3 Columns at one time- MD, DT1, RHOB1 )
fig, ax = plt.subplots()

# Adding Grids to the Plot
ax.grid(True)

# Removing first row since it has Units (ft, us/ft, g/cc) and showing the figure
ax.boxplot(np.array(excel_file_1)[1:]) 
plt.show()


# Extracting Column C RHOB1(g/cc) from Sheet
C_column = np.array(excel_file_1['RHOB1'][1:]).astype(np.float64)



## Box Plot for Column C (Rhob1) in the Sheet.
#Creating another axes, figure objects
fig2, ax2 = plt.subplots()

# Adding Grids to the Plot
ax2.grid(True)

# Setting y-axis range(0, 250)
ax2.set_ylim(0, 250)

# Showing the Plot
ax2.boxplot(C_column)
plt.show()