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
print(f"mycode time= {timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=1)}")

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

print(f"mycode2 time= {timeit.timeit(stmt=MYCODE2, number=1)}")

print(f"mycode3 time= {timeit.timeit(setup=MYSETUP2, stmt=MYCOD3, number=1)}")


MYSETUP3 = '''
import random
'''

MYCOD4 = '''
MILLION_RANDOM_NUMBERS = []
def MilRandNums(arr):
    for x in range(1000000):
        arr.append(random.random())
    return arr

MILLION_RANDOM_NUMBERS = MilRandNums(MILLION_RANDOM_NUMBERS)
sorted(MILLION_RANDOM_NUMBERS)
'''

MYCOD5 = '''
MILLION_RANDOM_NUMBERS = []
def MilRandNums(arr):
    for x in range(1000000):
        arr.append(random.random())
    return arr

MILLION_RANDOM_NUMBERS = MilRandNums(MILLION_RANDOM_NUMBERS)
MILLION_RANDOM_NUMBERS.sort()
'''

print(f"mycode4 time= {timeit.timeit(setup=MYSETUP3, stmt=MYCOD4, number=1)}")
print(f"mycode5 time= {timeit.timeit(setup=MYSETUP3, stmt=MYCOD5, number=1)}")
