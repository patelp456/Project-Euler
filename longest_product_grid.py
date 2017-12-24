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

fname = sys.argv[1]
data = np.loadtxt(fname)
print data.shape
product = 0

for i in range(0,data.shape[0]-4+1):
	for j in range(0,data.shape[0]-4+1):
		temp = data[i,j]*data[i+1,j+1]*data[i+2,j+2]*data[i+3,j+3]
		product = max(product,temp)

print product