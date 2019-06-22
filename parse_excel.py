#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
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
from tkinter import StringVar


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


def getExcel():
    ''' get excel data '''



def getCountry():
    countryStr = str(cntry.get())
    # print(countryStr)
    return countryStr


def main():
    ''' main '''
    global cntry

    root = tk.Tk()
    root.title("Parse Excel")

    cntry = tk.StringVar()

    lbCountry = tk.Label(root, text='Country')
    lbCountry.pack(side=tk.LEFT, padx=5, pady=5)
    eCountry = tk.Entry(root, textvariable=cntry)
    eCountry.pack(side=tk.LEFT, padx=5, pady=5)

    getCountryButton = tk.Button(root, text='GetCountry', command=getCountry)
    getCountryButton.pack(side=tk.LEFT, padx=5, pady=5)

    # canvas1 = tk.Canvas(root, width=300, height=300, bd=0,
    #                     bg=args.color, cursor='arrow')
    # canvas1.pack()

    # # excel select file
    # browseButton_Excel = tk.Button(text='Import Excel File', command=getExcel,
    #                             bg='green', fg='white', font=('Menlo', 12, 'bold'))
    # # canvas1.create_window(150, 150, window=browseButton_Excel)
    # browseButton_Excel.pack(side=tk.LEFT, padx=5, pady=5)
    import_path = filedialog.askopenfilename()

    # open workbook
    book = xlrd.open_workbook(import_path,
                              logfile=logf, verbosity=args.verbose)

    sheet = book.sheet_by_name("Table 9 ")

    data = {}
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
            }
        }

        if country == "Zimbabwe":
            break

    # pprint.pprint(data[args.country])
    pprint.pprint(data[getCountry()])


    b2 = tk.Button(root, text='Quit', command=root.quit)
    b2.pack(side=tk.RIGHT, padx=5, pady=5)

    root.mainloop()


if __name__ == '__main__':
    main()
