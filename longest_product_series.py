#!/usr/bin/env python

# ========= Import required modules =====================

# for using system commands
import sys

# for using os commands like list directeries etc
import os

# for mathematical functions specially matriices
import numpy as np

# for general maths
from math import *

fname = sys.argv[1]
data = np.loadtxt(fname, dtype = "string")
data = str(data)
data = list(data)
# print data
ans = 0

digits = input("enter the req number of contiguous digits")

for i in range(0,len(data)-digits + 1):
	temp = np.array(data[i:i+digits]).astype(int)
	ans = max(ans, np.prod(temp))
	print temp, ans
