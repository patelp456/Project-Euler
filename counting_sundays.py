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

days = 0
sundays = 0
start = 2
# sunday is day 7
for i in range(1901,2001):
    
    if i % 400 == 0:
        if start == 0:
            sundays += 3
        elif start == 3 or start == 1 or start == 4:
            sundays += 2
        else:
            sundays += 1
        start = (start + 2) % 7
    elif i % 100 ==0:
        if start == 4:
            sundays += 3
        elif start == 0 or start == 1 or start == 2:
            sundays += 2
        else:
            sundays += 1
        start = (start + 1) % 7
    elif i % 4 == 0:
        if start == 0:
            sundays += 3
        elif start == 3 or start == 1 or start == 4:
            sundays += 2
        else:
            sundays += 1
        start = (start + 2) % 7
    else :
        if start == 4:
            sundays += 3
        elif start == 0 or start == 1 or start == 2:
            sundays += 2
        else:
            sundays += 1
        start = (start + 1) % 7
    # print start,
print sundays
