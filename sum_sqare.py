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

n = input("enter the number : ")

sum_sq = (n*(n+1)/2)**2
sq_sum = n*(n+1)*(2*n + 1)/6
ans = sum_sq - sq_sum

print ans