#!/usr/bin/env python
# -*- coding: windows-1252 -*-
'''
_ex_diction.py

'''

from operator import attrgetter, itemgetter
from pprint import pprint


d1 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": [1964, 1965, 1966]
}

d2 = {
    "id": [1, 2, 3, 4, 5, 6],
    "brand": "Toyota",
    "model": "Corolla",
    "year": [1984, 1995, 1999, 2010, 2012, 2018]
}

d3 = {
    'make': [
        {
            "id": [1, 2, 3, 4, 5, 6],
            "brand": "Toyota",
            "model": "Corolla",
            "year": [1984, 1995, 1999, 2010, 2012, 2018]
        },
        {
            "brand": "Ford",
            "model": "Mustang",
            "year": [1964, 1965, 1966]
        }
    ]
}

pprint(d1, indent=2)
pprint(d2, indent=2)
pprint(d3, indent=4)

print(d1["year"][:2])
print(d2["id"][2:], d2["year"][2:])

sort_mdl = sorted(d3['make'], key=itemgetter('model'))
pprint(sort_mdl, indent=4)

for i, elem in enumerate(sort_mdl):
    print(i, elem['model'])

[print(i, elem['model']) for i, elem in enumerate(sort_mdl)]

#  print(d3['make'])
