#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 22:45:31 2023

@author: vinay
"""

# Importing the Required Packages
import pandas as pd
import os


# Getting the Excel File Paths from Datasets to Read
assign_folder_path = os.path.dirname(os.path.dirname(os.getcwd()))
ExcelTestData1_path = assign_folder_path+'/Assignment_Data_&_References/Example_Data_V2/ExcelTestData1.xlsx'
ExcelTestData2_path = assign_folder_path+'/Assignment_Data_&_References/Example_Data_V2/ExcelTestData2.xlsx'
ExcelTestData4_path = assign_folder_path+'/Assignment_Data_&_References/Example_Data_V2/ExcelTestDatat4.xlsx'


# Reading the Three Excel Files and getting Sheet1 in all
excel_file_1 = pd.read_excel(ExcelTestData1_path, sheet_name='Sheet1')
excel_file_2 = pd.read_excel(ExcelTestData2_path, sheet_name='Sheet1')
excel_file_4 = pd.read_excel(ExcelTestData4_path, sheet_name='Sheet1')



# Printing Rows in Excel File 1
for index, row in excel_file_1.iterrows():
    print(row.values)


# Printing Rows in Excel File 2 
for index, row in excel_file_2.iterrows():
    print(row.values)
    
# Printing Rows in Excel File 4
for index, row in excel_file_4.iterrows():
    print(row.values)
