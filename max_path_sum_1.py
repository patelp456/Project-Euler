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
data = []
with open(fname) as input_file:
    for i, line in enumerate(input_file):
        data.append(map(int, line.split(' ')))
# print len(data)
memo = {}
def calc_sum(i,j,m,n,memo) :
    if n < 0 or n > m :
        return 0
    if ((i,j),(m,n)) in memo :
        return memo[((i, j), (m, n))]
    if (i,j) == (m,n) :
        return data[i][j]
    else:
        t1 = calc_sum(i,j,m-1,n,memo)
        t2 = calc_sum(i,j,m-1,n-1,memo)
        # return max(t1, t2) + data[m][n]
        memo[((i, j), (m, n))] = max(t1,t2) + data[m][n]
        # print str(((i, j), (m, n))), memo[((i, j), (m, n))]
        return memo[((i, j), (m, n))]

result = 0

for k in range(0,len(data)):
    temp = calc_sum(0,0,14,k,memo)
    result = max(temp,result)

print result
