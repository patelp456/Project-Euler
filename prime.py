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

n = input("Enter the number : ")

prime_num = [2]
count = 1

i = 3

while len(prime_num) < n:
	flag = 0
	for num in prime_num :
		if i%num == 0:
			flag = 1
			break;

	if flag == 0:
		prime_num.append(i)
	i += 2

print prime_num


# ===== primality testing (solution from eular project) =====
# let say n is a number to be tested
# note tha fact that any prime > 3 can be written in the form of 6k + 1, or 6k - 1

def primality(n):
	if n == 1:
		return False
	elif n < 4:
		return True
	elif n%2 == 0:
		return False
	elif n < 9:
		return True
	elif n%3 == 0:
		return False
	else:
		limit = sqrt(n)
		p = 5
		while p <= limit:
			if n%p == 0:
				return False
			if n%(p+2) == 0:
				return False
			p += 6
	return True

i = 1
count = 0
while count < n:
	if primality(i) :
		count += 1
		print i,
	i += 1
