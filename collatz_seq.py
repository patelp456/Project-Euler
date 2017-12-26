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
for i in range(100000,1000000):
    num = i
    count = 1
    while num != 1:
        if num %2 == 0:
            num = num/2
        else:
            num = 3*num + 1
        count += 1
    if count > ans:
        print i,count
        ans = count