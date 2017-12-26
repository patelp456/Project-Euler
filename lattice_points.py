#!/usr/bin/env python

# ========= Import required modules =====================
# question is not clear

# for using system commands
import sys

# for using os commands like list directeries etc
import os

# for mathematical functions specially matriices
import numpy as np

# for general maths
from math import * 

m,n = input("enter comman separated - number of rows and columns in the grid : ")

arr = np.zeros((m+1,n+1),dtype=int)
arr[0,:] = 1
arr[:,0] = 1

for i in range(1,m+1):
    for j in range(1,n+1):
        arr[i,j] = arr[i-1,j] + arr[i,j-1]

print arr[m,n]