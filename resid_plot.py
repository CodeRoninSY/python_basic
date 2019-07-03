#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
resid_plot.py

Synopsis: Plot of output data using matplotlib

Author: CodeRoninSY
Date: <2019-07-02>

Methods:
1. resid_post(residfile)    : residuals plot (particularly for steady-state)
2. out_post(outfile)        : x-fi plot from output file

"""
import functools
import numpy as np
import matplotlib.pyplot as plt
import glob
import time
import argparse
import subprocess
import platform
from pprint import pprint


__author__ = "CodeRoninSY"
__date__ = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
__version__ = 0.1


def timeit(func):
    """ timeit """
    @functools.wraps(func)
    def w_timeit(*args, **kwargs):
        strtm = time.perf_counter()
        valtm = func(*args, **kwargs)
        endtm = time.perf_counter()
        rettm = endtm - strtm
        print(f"Finished {func.__name__!r} in {rettm:.3f} sec.")
        return valtm
    return w_timeit


@timeit
def resid_post(residf=None):
    "resid.out postprocess"
    resdata = np.genfromtxt(residf, comments='#', delimiter=',', autostrip=True, skip_header=1, skip_footer=0, names=['ITER', 'RESIDUAL'])

    print(f"DataType: {type(resdata)}, {resdata.shape}")
    pprint(resdata)
    x = resdata['ITER']
    y = resdata['RESIDUAL']

    fig, ax1 = plt.subplots()
    ax1.semilogy(x, y, label="Residual")

    ax1.legend(loc="best")
    ax1.set_xlabel("ITER")
    ax1.set_ylabel("Residual")
    ax1.set_title("1D convection-diffusion equation")
    ax1.grid()

    fig.savefig(residf + ".png")
    # plt.show()


@timeit
def out_post(outf=None, soltype=None):
    """
    output file postprocess
    soltype = 0 -> unsteady solution out file plot
    soltype = 1 -> steady-state solution out (*.csv) file plot
    """
    if (soltype == 0):
        data = np.genfromtxt(outf, comments='#', delimiter=',', skip_header=12,
        skip_footer=0, names=['X', 'FI'], autostrip=True)
    elif (soltype == 1):
        data = np.genfromtxt(outf, comments='#', delimiter=',', skip_header=1,
                             skip_footer=0, names=['X', 'FIEX', 'FI', 'ERROR'], autostrip=True)

    print(f"DataType: {type(data)}, {data.shape}")
    pprint(data)

    if (soltype == 0):
        x = data['X']
        y = data['FI']
    elif (soltype == 1):
        x = data['X']
        y = data['FI']

    fig, ax = plt.subplots()
    ax.plot(x, y, label="fi")

    ax.legend(loc="best")
    ax.set_xlabel("X()")
    ax.set_ylabel("FI()")
    ax.set_title("1D convection-diffusion equation")
    ax.grid()

    fig.savefig(outf + ".png")
    # plt.show()


@timeit
def main():
    # clear screen
    if platform.system() == "Windows":
        subprocess.Popen("cls", shell=True).communicate()
    elif platform.system() == "Linux":
        subprocess.Popen("clear", shell=True).communicate()
    # read data files
    residf = glob.glob(args.resid)
    outf = glob.glob(args.out)

    print("resid=> ", residf)
    print("outf=> ", outf)

    if (args.steady == 0):
        out_post(outf[0], args.steady)
    elif (args.steady == 1):
        out_post(outf[0], args.steady)
        resid_post(residf[0])


if __name__ == "__main__":
    """ MAIN driver """
    parser = argparse.ArgumentParser(
        description="Plotlib Utility for 1D conv-diff eq solver.")
    parser.add_argument(
        '-o', '--out', type=str, default='p1ds.out',
        help='Output file.')
    parser.add_argument(
        '-r', '--resid', nargs='?', default='residual.csv', help='Residual file')
    parser.add_argument(
        '-s', '--steady', default=0, type=int,
        help='Select out or resid plot according to analysis type.')
    args = parser.parse_args()

    main()
