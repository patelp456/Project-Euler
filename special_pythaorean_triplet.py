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
limit = int(sqrt(1000)) + 1
for m in range(0,limit):
    for n in range(0,limit):
        if m*n + m**2 == 1000 and m > n:
            print m * n * (m**2 - n**2) * (m**2 + n**2) * 0.25
