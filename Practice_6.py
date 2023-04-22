#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 23:24:11 2023

@author: vinay
"""

# Importing the Required Packages
import matplotlib.pyplot as plt
import numpy as np


# Getting Random Numpy array X with size 100 - values range from 0-1000 
X = np.random.randint(0, 1001, size=100)

# Getting Random Numpy array Y with size 100 - values range from 0-50 
Y = np.random.randint(0, 51, size=100)

# Sorting the Arrays in Ascending Order to the Required Progressive Diagonal Line Plot
X.sort()
Y.sort()

# Setting the x-axis and y-axis range (0-1000) and (0-50) respectively.
plt.xlim(0, 1000)
plt.ylim(0, 50)

# Labeling the x-axis and y-axis as X and Y respectively.
plt.xlabel('X')
plt.ylabel('Y')

# Naming Plot Title as 'X-Y Plot'
plt.title('X-Y Plot')

print('PLOT 1 with Random Numbers')
# Showing the Plot.
## This Plot is with Random Numbers Generated X(0-1000) and Y(0-50). It will Vary for everytime we Run and Check Plot.
plt.plot(X, Y, color='blue')
plt.show()


print('PLOT 2 with Fixed Numbers')

# If we want the Straight Diagonal Plot with X and Y
plt.xlim(0, 1000)
plt.ylim(0, 50)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('X-Y Plot')
plt.plot([0, 1000], [0, 50], color='blue')