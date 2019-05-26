#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
iterable.py

From Nina Zakharenko: Elegant solutions for everyday Python problems
https://www.youtube.com/watch?v=WiQqqB9MlkA
# in order to be iterable, a class needs to implement __iter__()
# __iter__() must return an iterator
# in order to be an iterator a class needs to implement __next__() ...
# .. which must raise StopIteration when there are no more items to return
'''
from pprint import pprint, pformat

class IterableServer:

    services = [
            { 'active': False, 'protocol': 'ftp', 'port': 21 },
            { 'active': True, 'protocol': 'ssh', 'port': 22 },
            { 'active': True, 'protocol': 'http', 'port': 80 },
    ]

    def __init__(self):
        self.current_pos = 0

    def __iter__(self):
        for service in self.services:
            if service['active']:
                yield service['protocol'], service['port']

    def __next__(self):
        while self.current_pos < len(self.services):
            service = self.services[self.current_pos]
            self.current_pos + 1
            if service['active']:
                return service['protocol'], service['port']
            raise StopIteration


for protocol, port in IterableServer():
    print('service %s on port %d' % (protocol, port))

iter_srv = IterableServer()

my_isrv = (itr for itr in iter_srv)

for _c in range(len(iter_srv.services)):
    print(_c, next(my_isrv))

# # use single parenthesis () to create a generator comprehension
# my_gen = (num for num in range(3))

# print(my_gen)
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
