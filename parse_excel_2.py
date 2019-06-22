#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    parse_excel_2.py

    Synopsis: Tkinter GUI app for parse excel file

    This is a script to parse child labor and child marriage data.
    The excel file used in this script can be found here:
        http://www.unicef.org/sowc2014/numbers/

    Author: CodeRoninSY
    Date: <2019-06-22>
"""

import argparse
import xlrd
import pprint
import tkinter as tk
from tkinter import filedialog


# logfile for excel read log
logf = open("logfile.out", "w")

# parser for verbosity levels
parser = argparse.ArgumentParser(description='Log verbose to out.')
parser.add_argument('-v', '--verbose', type=int, default=0,
                    help='integer for verbosity level')
parser.add_argument('-c', '--country', type=str, default="Turkey", help='string for country')
parser.add_argument('-C', '--color', type=str,
                    default='turquoise', help='string for bg color')
args = parser.parse_args()

# Data to be read from Excel
data = {}

# hardcoded sheetname from Excel file
OPTIONS = [
    "Table 9 ",
]


def getData():
    ''' getData (Country) '''
    pprint.pprint(data[getCountry()], indent=4)


def getCountry():
    ''' get Country '''
    countryStr = str(cntry.get())
    pprint.pprint(countryStr)
    return countryStr


def excelRead():
    ''' main '''
    import_path = filedialog.askopenfilename()

    # open workbook
    book = xlrd.open_workbook(import_path,
                              logfile=logf, verbosity=args.verbose)

    sheet = book.sheet_by_name(OPTIONS[0])

    for i in range(14, sheet.nrows):

        # Start at 14th row, because that is where the countries begin
        row = sheet.row_values(i)

        country = row[1]

        data[country] = {
            'child_labor': {
                'total': [row[4], row[5]],
                'male': [row[6], row[7]],
                'female': [row[8], row[9]],
            },
            'child_marriage': {
                'married_by_15': [row[10], row[11]],
                'married_by_18': [row[12], row[13]],
            },
            'birth_registration': {
                'birth_reg_total': [row[14], row[15]],
            },
            'female_genital_mutilation': {
                'prevalence_women': [row[16], row[17]],
                'prevalence_girls': [row[18], row[19]],
                'attitudes': [row[20], row[21]],
            },
            'justification_wife_beating': {
                'male': [row[22], row[23]],
                'female': [row[24], row[25]],
            },
            'violent_discipline': {
                'total': [row[26], row[27]],
                'male': [row[28], row[29]],
                'female': [row[30], row[31]],
            }
        }

        if country == "Zimbabwe":
            break


if __name__ == '__main__':
    ''' main driver '''
    # country name global
    global cntry
    global sheetname

    # root window
    root = tk.Tk()
    root.title("Parse Excel")

    # text entry
    cntry = tk.StringVar()

    # sheet name set from OPTIONS
    sheetname = tk.StringVar(root)
    sheetname.set(OPTIONS[0])

    # browse excel file
    browseButton_Excel = tk.Button(text='Import Excel File', command=excelRead,
                                bg='green', fg='white', font=('helvetica', 12, 'bold'))
    browseButton_Excel.pack(side=tk.LEFT, padx=5, pady=5)

    sh = tk.OptionMenu(root, sheetname, OPTIONS[0])
    sh.pack(side=tk.LEFT, padx=2, pady=2)

    lbCountry = tk.Label(root, text='Country')
    lbCountry.pack(side=tk.LEFT, padx=5, pady=5)
    eCountry = tk.Entry(root, textvariable=cntry)
    eCountry.pack(side=tk.LEFT, padx=5, pady=5)
    # get data
    getData = tk.Button(root, text='GetData', command=getData,
                        bg='teal', fg='white', font=('helvetica', 12, 'bold'))
    getData.pack(side=tk.LEFT, padx=5, pady=5)

    b2 = tk.Button(root, text='Quit', command=root.quit)
    b2.pack(side=tk.RIGHT, padx=5, pady=5)

    root.mainloop()
