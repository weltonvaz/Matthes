#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

cls()

from sympy import isprime

for n in range(74207281,80000000,2):
	d = divmod(2**(n-1),n)
	if d[1] == 1:
		e0 = bin(d[0])
		f = e0.count('1')
		e1 = bin(d[1])
		g = e0.count('0')-1
		if f+g >= 25:
			if isprime(n) == True:
				h = str((2**n)-1)
				if h[-1] == str('1') or h[-1] == str('7'):
					print(n)
				
