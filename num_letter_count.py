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

data = {
        'one' : 3, 
        'two' : 3, 
        'three' : 5, 
        'four' : 4, 
        'five': 4, 
        'six': 3,
        'seven':5,
        'eight':5,
        'nine':4,
        'ten':3,
        'eleven':6,
        'twelve':6,
        'thirteen' : 8,
        'fourteen' : 8,
        'fifteen' : 7,
        'sixteen' : 7,
        'seventeen' : 9,
        'eighteen' : 8,
        'nineteen' : 8,
        'twenty' : 6,
        'thirty':6,
        'forty':5,
        'fifty':5,
        'sixty':5,
        'seventy':7,
        'eighty':6,
        'ninety':6,
        'hundred':7,
        'thousand':8,
        'and':3 }

m,n = input("Enter comma separated range between 1 and 1000  e.g. 1,10 : ")
total = 0
for i in range(m,n+1):
    place = 1
    num = i
    while num != 0:
        if place == 1 and (num%100 <= 20) :    
            if num % 100 == 1:
                total += data['one']
            elif num % 100 == 2:
                total += data['two']
            elif num % 100 == 3:
                total += data['three']
            elif num % 100 == 4:
                total += data['four']
            elif num % 100 == 5:
                total += data['five']
            elif num % 100 == 6:
                total += data['six']
            elif num % 100 == 7:
                total += data['seven']
            elif num % 100 == 8:
                total += data['eight']
            elif num % 100 == 9:
                total += data['nine']
            elif num % 100 == 10:
                total += data['ten']
            elif num % 100 == 11:
                total += data['eleven']
            elif num % 100 == 12:
                total += data['twelve']
            elif num % 100 == 13:
                total += data['thirteen']
            elif num % 100 == 14:
                total += data['fourteen']
            elif num % 100 == 15:
                total += data['fifteen']
            elif num % 100 == 16:
                total += data['sixteen']
            elif num % 100 == 17:
                total += data['seventeen']
            elif num % 100 == 18:
                total += data['eighteen']
            elif num % 100 == 19:
                total += data['nineteen']
            elif num % 100 == 20:
                total += data['twenty']
            else:
                pass
            num = num/10
            place += 1
        elif place == 1 and num%100 > 20:
            if num % 10 == 1:
                total += data['one']
            elif num % 10 == 2:
                total += data['two']
            elif num % 10 == 3:
                total += data['three']
            elif num % 10 == 4:
                total += data['four']
            elif num % 10 == 5:
                total += data['five']
            elif num % 10 == 6:
                total += data['six']
            elif num % 10 == 7:
                total += data['seven']
            elif num % 10 == 8:
                total += data['eight']
            elif num % 10 == 9:
                total += data['nine']
            else:
                pass
        elif place == 2:
            if num%10 == 2:
                total += data['twenty']
            elif num%10 == 3:
                total += data['thirty']
            elif num%10 == 4:
                total += data['forty']
            elif num%10 == 5:
                total += data['fifty']
            elif num%10 == 6:
                total += data['sixty']
            elif num%10 == 7:
                total += data['seventy']
            elif num%10 == 8:
                total += data['eighty']
            elif num%10 == 9:
                total += data['ninety']
            else:
                pass
        elif place == 3 and num%10 != 0:
            total += data['hundred']
            if i % 100 != 0:
                total += data['and']
            if num % 10 == 1:
                total += data['one']
            elif num % 10 == 2:
                total += data['two']
            elif num % 10 == 3:
                total += data['three']
            elif num % 10 == 4:
                total += data['four']
            elif num % 10 == 5:
                total += data['five']
            elif num % 10 == 6:
                total += data['six']
            elif num % 10 == 7:
                total += data['seven']
            elif num % 10 == 8:
                total += data['eight']
            elif num % 10 == 9:
                total += data['nine']
            else:
                pass
        if place == 4:
            total += data['one'] + data['thousand']
        num = num/10
        place += 1
    print i, total
