#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
argp_csvDatafrm.py

Dev: CodeRoninSY
Date: <2020-10-26>

Synopsis: Read Titanic passenger csv and postprocess the data.
        Use PySimpleGUI for selecting csv file and maybe other
        input parameters.

I/O:
args.data       : data[0] = col1 (X)
                 data[1] = col2 (Y)
'''

import os
import csv
import argparse
import pandas as pd
import matplotlib.pyplot as plt
import PySimpleGUI as sg

# arguments parser
parser = argparse.ArgumentParser(prog='argp_csvDatafrm', description='Dataframe from a csv')
parser.add_argument(
    '-d', '--data', type=int, nargs='+', metavar='Col1 Col2', help='Column key number', default=[0, 8], required=False)
parser.add_argument('-f', '--file', type=str, nargs='?', metavar='_test', help='Excel file name prefix only', default='_test')
group = parser.add_mutually_exclusive_group()
group.add_argument('-q', '--quiet', action='store_true', help='Print file name quiet')
group.add_argument('-v', '--verbose', action='store_true', help='Print output verbose')
args = parser.parse_args()


# titanic_parse
def titanic_parse(col1=None, col2=None, xlFile=None):
    ''' columns to process for Titanic public csv '''
    if xlFile == '':
        msg = "%s is None" % xlFile
        raise argparse.ArgumentTypeError(msg)
    xlfx = xlFile + ".xlsx"

    sg.theme('DarkGrey1')

    layout = [
        [sg.Text('Filename')],
        [sg.Input(), sg.FileBrowse(file_types=
                    (("CSV files", "*.csv"),))],
        [sg.OK(), sg.Cancel()]
    ]

    sg.popup('*** Titanic Data ***', auto_close=True,
            auto_close_duration=1)

    window = sg.Window('Get csv filename', layout)

    event, values = window.read()
    window.close()
    return [event, values, xlfx]


# main()
if __name__ == "__main__":
    ''' MAIN driver '''
    [event, values, xlfx] = titanic_parse(*args.data, args.file)
    if args.quiet:
        print(event, xlfx)
    elif args.verbose:
        print("Column names are [ %d ] and [ %d ], and \
            \nExcel file prefix is [ %s ] \
            \nCSV read file name is [ %s ]" % \
            (args.data[0], args.data[1], xlfx, values[0]))
    else:
        print("Titanic data = {%s, %s}" % (event, values[0]))
