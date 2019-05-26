#!/usr/bin/env python
''' randoms.py '''

import functools
import time
import random
from typing import List
from clint.textui import progress, colored, puts, prompt, validators
from pyfiglet import Figlet

# number of elements
ELEMRNG: int = 1000000


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

MIL_RAND_NUM: Vector = []

# @timeit
def MilRandNums(arr: Vector) -> Vector:
    for x in range(ELEMRNG):
        arr.append(random.random())
    return arr


if __name__ == '__main__':
    ''' potpouri of CLI and function features '''
    f = Figlet(font='poison')
    # print(f.renderText('Randoms'))
    puts(colored.red(f.renderText('Randoms')))

    # Standard non-empty input
    name = prompt.query("What's your name?")

    # Set validators to an empty list for an optional input
    language = prompt.query("Your favorite tool (optional)?", validators=[])

    # Shows a list of options to select from
    inst_options = [{'selector':'1','prompt':'Full','return':'full'},
                    {'selector':'2','prompt':'Partial','return':'partial'},
                    {'selector':'3','prompt':'None','return':'no install'}]
    inst = prompt.options("Full or Partial Install", inst_options)

    # Use a default value and a validator
    path = prompt.query('Installation Path', default='/usr/local/bin/', validators=[validators.PathValidator()])

    puts(colored.blue('Hi {0}. Install {1} {2} to {3}'.format(name, inst, language or 'nothing', path)))

    strt = time.clock()
    MIL_RAND_NUM = MilRandNums(MIL_RAND_NUM)
    endt = time.clock()
    print(f"Runtime >> {endt - strt} sec")

    strt = time.clock()
    sorted(MIL_RAND_NUM)
    endt = time.clock()
    print(f"Runtime >> {endt - strt} sec")

    for i in progress.bar(range(30)):
        MIL_RAND_NUM = MilRandNums(MIL_RAND_NUM)
