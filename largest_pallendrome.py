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
ans = 0

for i in range(100,1000):
	for j in range(100,1000):
		num = i*j
		temp = str(num)
		if temp == temp[::-1] :
			ans = max(ans,num)
			print ans,