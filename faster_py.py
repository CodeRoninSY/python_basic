#!/usr/bin/env python3
''' faster_py.py

Write faster python

Excerpts from Sebastian Witowski - Europython 2016 conference

'''

import functools
import time
import numpy as np
import timeit
import random


def timer(func):
    ''' print the runtime of the decorated func '''
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer
#
#
#  # permissions or forgiveness?
#  class Foo(object):
#      hello = 'World'
#      def foo(self):
#          return f"{self.foo} is called"
#      def bar(self):
#          return f"{self.bar} is called"
#      def baz(self):
#          return f"{self.baz} is called"
#
#
#  fuz = Foo()
#
#  if hasattr(fuz, 'hello'):
#      print(f"hasattr {fuz.hello}")
#  # ~149ns
#
#
#  if (hasattr(fuz, 'foo') and hasattr(fuz, 'bar')
#      and hasattr(fuz, 'baz')):
#      print(f"hasattr {fuz.foo!r}")
#      print(f"hasattr {fuz.bar!r}")
#      print(f"hasattr {fuz.baz!r}")
#
#
#  try:
#      print(f"{fuz.hello!r}")
#  except AttributeError:
#      pass
#  # 43.1 ns 3.5x faster
#
#  # exception handling is generally expensive
#  try:
#      fuz.foo()
#      fuz.bar()
#      fuz.baz()
#  except AttributeError:
#      pass


@timer
def MakeRandArr(array):
    for x in range(1000000):
        array.append(random.random())
    return array

RandArray = []
RandArray = MakeRandArr(RandArray)


@timer
def sortArray(array):
    return array.sort()

SortRandArray = sortArray(RandArray)


# usage example of timeit function from timeit library
setup = '''
import numpy as np
'''

mystmt = '''
arr = np.arange(1000000)
millSET = set(arr)
999999 in millSET
'''

print(timeit.timeit(setup=setup, stmt=mystmt, number=1))
