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

limit = int(sys.argv[1])
a = 1
b = 2
total_even = b
# print a , b ,

while(b < limit):
	temp = b
	b = b + a
	a = temp
	if b%2 == 0 and b < limit:
		total_even += b
	# print b,
print total_even