#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import argparse
from pprint import pprint

# argparser for csv read
parser = argparse.ArgumentParser(description='Parse data from CSV file read.')
parser.add_argument('-c', '--country', type=str,
                    default="Turkey", help='Country [str]')
parser.add_argument('-y', '--year', type=str,
                    default='2012', help='Year [str]')
args = parser.parse_args()

# csvfile = open('../../data/chp3/data-text.csv', 'r')
# reader = csv.DictReader(csvfile)
# for line in reader:
#     print(line)

# for i, row in enumerate(reader):
#     if (row['Country'] == 'Turkey' and row['Year'] == '1990'):
#         print(i, " >> ", row, end='\n')

with open('../../data/chp3/data-text.csv', 'r') as f:
    for i, line in enumerate(csv.DictReader(
        f, fieldnames=('Indictr', 'Publish', 'Year', 'Region', 'IncomGrp',
        'Cntry', 'Sex', 'DispVal', 'Numer', 'Low', 'High', 'Comm'))):
        if (line['Cntry'] == args.country and line['Year'] == args.year):
            print(f"r: {i} __ {line['Cntry']}, {line['Indictr']}, {line['Year']}, {line['Sex']}, {line['Numer']}")
