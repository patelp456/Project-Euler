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

num = int(sys.argv[1])
limit = int(sqrt(num)) + 10
factor_old = factor_new = 1

while num%2 == 0:
	num = num/2
	factor_new = 2
if factor_old != factor_new:
	print factor_new,

for i in range(3, limit, 2):
	while  num%i == 0:
		num = num/i
		factor_old = factor_new
		factor_new = i
		# if factor_old != factor_new:
		print factor_new,

if num != 1:
	print num