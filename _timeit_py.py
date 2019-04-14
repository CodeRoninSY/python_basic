#!/usr/bin/env python
''' _timeit_py.py '''

# importing the required module
import timeit

# code snippet to be executed only once
MYSETUP = "from math import sqrt"

# code snippet whose execution time is to be measured
MYCODE = '''
def example():
    mylist = []
    for x in range(1000000):
        mylist.append(sqrt(x))
'''

# timeit statement
print(timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=1))

MYCODE2 = '''
MILLION_NUMS = list(range(1000000))
500000 in MILLION_NUMS
'''

MYSETUP2 = '''
import numpy as np
'''
MYCOD3 = '''
arr = np.arange(1000000)
MIL_SET = set(arr)
999999 in MIL_SET
'''

print(timeit.timeit(stmt=MYCODE2, number=1))

print(timeit.timeit(setup=MYSETUP2, stmt=MYCOD3, number=1))
