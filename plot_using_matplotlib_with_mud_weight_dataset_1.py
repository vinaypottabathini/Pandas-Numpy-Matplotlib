#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 15:40:54 2023

@author: vinay
"""
#Read the “Mud_Weight.csv” file in python.
#Create a Plot using matplotlib like the sample on right


# Importing the required packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


# Getting the File Path from Datasets to Read
assign_folder_path = os.path.dirname(os.path.dirname(os.getcwd()))
file_path = assign_folder_path+'/Assignment_Data_&_References/Datasets/Mud_Weight.csv'


# Reading the Mud_Weight.csv file using pandas read_csv
# Slicing the first row at 0 index to remove the units MD-'m' and Mud_Weight - 'lbm/galUS'
data = pd.read_csv(file_path, delimiter=',', usecols=['MD', 'Mud_Weight']).values[1:]

# Converting the data to respective types as they are in strings while we read
data[:, 0] = data[:, 0].astype(int)
data[:, 1] = data[:, 1].astype(float)

# Sorting the data
# Sorting MD-m units in Descending Order and Mud_Weight-lbm/galUS unit in Ascending to meet output graph line
y_axis_list = sorted(data[:, 1], reverse=True)
x_axis_list =  sorted(data[:, 0])


# Creating a figure with one subplot with matplotlib
fig, ax = plt.subplots()

# Changing the background color of plot to blue
ax.set_facecolor('#0000FF')

# Using the marker color as yellow and size -100.
# Showing the Figure.
ax.plot(x_axis_list, y_axis_list, 'yellow' , markersize=-100)
plt.show()
