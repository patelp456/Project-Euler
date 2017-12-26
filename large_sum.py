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
data = np.loadtxt(fname)
data = (data/10**49)
ans = str(sum(data))
print ans