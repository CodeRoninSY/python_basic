#!/usr/bin/env python
''' randoms.py '''

import functools
import time
import random
from typing import List
from clint.textui import progress
import click


def timeit(fn):
    ''' timeit '''
    @functools.wraps(fn)
    def wrapper_timeit(*args, **kwargs):
        stt = time.perf_counter()
        val = fn(*args, **kwargs)
        ent = time.perf_counter()
        rt = ent - stt
        print(f"Finished {fn.__name__!r} in {rt:.5f} sec.")
        return val
    return wrapper_timeit


Vector = List[int]

MILLION_RANDOM_NUMBERS: Vector = []

@timeit
def MilRandNums(arr: Vector) -> Vector:
    for x in range(1000000):
        arr.append(random.random())
    return arr


if __name__ == '__main__':
    strt = time.clock()
    MILLION_RANDOM_NUMBERS = MilRandNums(MILLION_RANDOM_NUMBERS)
    endt = time.clock()
    print(f"Runtime >> {endt - strt} sec")

    strt = time.clock()
    sorted(MILLION_RANDOM_NUMBERS)
    endt = time.clock()
    print(f"Runtime >> {endt - strt} sec")

    for i in progress.bar(range(10)):
        MILLION_RANDOM_NUMBERS = MilRandNums(MILLION_RANDOM_NUMBERS)
