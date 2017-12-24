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


def num_divisors(n,primes):
	record = {}
	divisors = 1
	
	for prime in primes:
		count = 0
		while n != 0 and n%prime == 0:
			n = n/prime
			try:
				record[prime] += 1
			except:
				record[prime] = 1

	for key in record:
		divisors = divisors*(record[key] + 1)

	return divisors

limit = input("number of divisors required : ")
# generate the list of first 500 prime numbers
i = 1
count = 0
primes = []
while count < 500:
	if primality(i) :
		count += 1
		# print i,
		primes.append(i)
	i += 1

divisors = 1
i = 1
while divisors < limit:
	n = i*(i+1)/2
	divisors = num_divisors(n,primes)
	i += 1
	print n, divisors