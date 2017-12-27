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

a = str(2**1000)
a = np.array(list(a))
a = a.astype(int)
# print a
print sum(a)