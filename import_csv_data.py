#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
import_csv_data.py

Synopsis: Import csv

Author: CodeRoninSY
Date: <2019-06-23>
"""
import argparse
import csv
from pprint import pprint


# argparser for csv read
parser = argparse.ArgumentParser(description='Parse data from CSV file read.')
parser.add_argument('-c', '--country', action='store', dest='list',
                            type=str, nargs='*', default=["Turkey","Italy","Germany", "Spain"], help='Country [str]')
parser.add_argument('-y', '--year', type=str,
                    default='2012', help='Year [str]')
args = parser.parse_args()

# reader object
csvfile = open('../../data/chp3/data-text.csv', 'r')
reader = csv.reader(csvfile)

print("List of items: {}".format(args.list))

for i, row in enumerate(reader):
    for cntry in args.list:
        if row[5] == cntry and row[2] == args.year:
            print(i, ' >> ', row[0], ':: ', row[5], row[6], row[7], row[8])
