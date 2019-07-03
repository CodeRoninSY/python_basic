#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
p1dus_v1.py

Synopsis: Unsteady 1D convection-diffusion equation with Dirichlet boundary conditions ..
.. on both ends.
Initial solution is zero field, boundary conditions are time-independent; the transition from initial to steady solution is simulated using different time integration schemes.

Author: CodeRoninSY
Date: <2019-07-01>
Version: 0.1

References:
[1] Computational Fluid Dynamics, Ferziger & Peric

Usage::
$> python p1dus_v1.py -h --> for help on arguments
$> python p1dus_v1.py -i parameter.json -o fileout -p 51

IO::
Input Data/File:
    1. parameter.json   = parameters json config file for parameters used in code

Output Data/File:
    1. fileout          = output written to "fileout" via -o, --output option

"""
import functools
from typing import List, Tuple, Dict, Any
import math
import time
import numpy as np
import argparse
import json
from pprint import pprint
import subprocess
import platform

__author__ = "CodeRoninSY"
__version__ = "0.1"
__date__ = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())


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


# InputParam object for reading JSON settings
class InputParam(object):
    """ Input Parameters from JSON file """

    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)

    def __str__(self):
        return f"TITLE:{self.title}, DENS={self.den}, VELO={self.vel}, DIFF={self.dif}, FI0={self.fi0}, FIN={self.fin}, SCHEME={self.ic}, XMIN={self.xmin}, XMAX={self.xmax}, EXPAN={self.ex}, N={self.n}, ISOLV={self.isolv}, OMEGA={self.omega}, EPSILON={self.epsil}, MAXIT={self.maxit}, ResidFile={self.residf}, ResultFile={self.rstout}"

    def __repr__(self):
        return str(self)


@timeit
def getParams(filename, raw=False):
    """ getParams function reads from parameter.json file """
    try:
        data = json.load(open(filename))
    except FileNotFoundError:
        return []
    else:
        if raw:
            return data["setting"]
        return [InputParam(**prm) for prm in data['setting']]


# SOLVERS
@timeit
def Jacobi():
    """ JACOBI Iterative Algorithm Subroutine """
    fio: float = np.zeros(NX)
    RES: float = 0.0
    ITER: int

    fout.write(f"ITER\t\tRESIDUAL\n")
    f_resd.write(f"ITER, RESIDUAL\n")
    print(f"ITER\t\tRESIDUAL")

    for ITER in range(1, MAXIT + 1):
        # save old solution
        for i in range(0, N):
            fio[i] = FI[i]
        # calculate new solution
        for i in range(1, NM):
            FI[i] = (
                - 1.0 * AE[i] * fio[i + 1] - AW[i] * fio[i - 1]
                + Q[i]) / AP[i]
        # calculate residual and check convergence
        RES = 0.0
        for i in range(1, NM):
            RES = RES + abs(
                - 1.0 * AE[i] * FI[i + 1] - AW[i] * FI[i - 1]
                + Q[i] - AP[i] * FI[i]
            )
        print(f"{ITER},\t{RES}")
        fout.write("{0},\t{1}\n".format(ITER, RES))
        f_resd.write(f"{ITER}, {RES}\n")
        if (RES < EPSIL):
            break


@timeit
def GaussSeidel():
    """ GAUß-SEIDEL Solver Subroutine """
    RES: float = 0.0
    ITER: int

    fout.write(f"ITER\t\tRESIDUAL\n")
    f_resd.write(f"ITER, RESIDUAL\n")
    print(f"ITER\t\tRESIDUAL")

    for ITER in range(1, MAXIT + 1):

        # calculate new solution
        for i in range(1, NM):
            FI[i] = (
                - 1.0 * AE[i] * FI[i + 1] - AW[i] * FI[i - 1] + Q[i]) / (AP[i])
        # calculate residual and check convergence
        RES = 0.0
        for i in range(1, NM):
            RES = RES + abs(
                - 1.0 * AE[i] * FI[i + 1] - AW[i] * FI[i - 1] + Q[i] - AP[i] * FI[i])

        print(f"{ITER},\t{RES}")
        fout.write("{0},\t{1}\n".format(ITER, RES))
        f_resd.write(f"{ITER}, {RES}\n")
        if (RES < EPSIL):
            break


@timeit
def GSOR():
    """ Gauß-Seidell Successive Over Relaxation Solver Subroutine """
    RES: float = 0.0
    ITER: int

    fout.write(f"ITER\t\tRESIDUAL\n")
    f_resd.write(f"ITER, RESIDUAL\n")
    print(f"ITER\t\tRESIDUAL")

    for ITER in range(1, MAXIT + 1):
        # calculate new solution
        for i in range(1, NM):
            FI[i] = FI[i] + OM * ((
                - 1.0 * AE[i] * FI[i + 1] - AW[i] * FI[i - 1] + Q[i]) / (AP[i]) - FI[i])
        # calculate residual and check convergence
        RES = 0.0
        for i in range(1, NM):
            RES = RES + abs(
                - 1.0 * AE[i] * FI[i + 1] - AW[i] * FI[i - 1] + Q[i] - AP[i] * FI[i])

        print(f"{ITER},\t{RES}")
        fout.write("{0},\t{1}\n".format(ITER, RES))
        f_resd.write(f"{ITER}, {RES}\n")
        if (RES < EPSIL):
            break


@timeit
def TDMA():
    """ TriDiagonal Matrix Algorithm Subroutine """
    bpr: float = np.zeros(NX)
    v: float = np.zeros(NX)

    for i in range(1, NM):
        bpr[i] = 1.0 / (AP[i] - AW[i] * AE[i - 1] * bpr[i - 1])
        v[i] = Q[i] - AW[i] * v[i - 1] * bpr[i - 1]

    for i in range(NM-1, 1, -1):
        FI[i] = (v[i] - AE[i] * FI[i+1]) * bpr[i]


# CLI argument parser for P1DS
parser = argparse.ArgumentParser(
    description="P1DS 1-D convection-diffusion equation solver.")
parser.add_argument('-o', '--output', type=str,
                    default='fileout', help="fileout output file.")
parser.add_argument('-p', '--parameter', type=int,
                    default=1001, help="NX parameter for max array lengths.")
parser.add_argument('-i', '--input', nargs='?', type=str,
                    default='parameter.json', help="parameter json file for input.")
args = parser.parse_args()


# MAIN Driver
if __name__ == "__main__":
    ''' MAIN driver '''

    # clear screen
    if platform.system() == "Windows":
        subprocess.Popen("cls", shell=True).communicate()
    elif platform.system() == "Linux":
        subprocess.Popen("clear", shell=True).communicate()

    print(f"\n\n<*  P 1 D S  *>\n\n")

    print(f"{__doc__}")
    print(f"Author: {__author__}")
    print(f"Version: {__version__}")
    print(f"Date: {__date__}")
    print("\n\n*** P 1 D S ***\n\n")

    # parameter NX
    NX: int = args.parameter
    # in/out filename
    FILOUT: str = args.output
    FILIN: str = args.input

    PARAMS = getParams(FILIN)
    RPARAMS = getParams(FILIN, raw=True)

    # pprint(PARAMS, indent=4)
    # pprint(RPARAMS, indent=4)

    # COMMON block
    N: int = 0
    NM: int = 0
    FI: float = np.zeros(NX)
    AE: float = np.zeros(NX)
    AW: float = np.zeros(NX)
    AP: float = np.zeros(NX)
    Q: float = np.zeros(NX)
    X: float = np.zeros(NX)
    FIEX: float = np.zeros(NX)
    np.array(FI, dtype=np.float64, ndmin=1)
    np.array(AE, dtype=np.float64, ndmin=1)
    np.array(AW, dtype=np.float64, ndmin=1)
    np.array(AP, dtype=np.float64, ndmin=1)
    np.array(Q, dtype=np.float64, ndmin=1)
    np.array(X, dtype=np.float64, ndmin=1)
    np.array(FIEX, dtype=np.float64, ndmin=1)

    # input settings
    DEN: float = RPARAMS[0]["den"]
    VEL: float = RPARAMS[0]["vel"]
    DIF: float = RPARAMS[0]["dif"]
    FI0: float = RPARAMS[0]["fi0"]
    FIN: float = RPARAMS[0]["fin"]
    IC: int = RPARAMS[0]["ic"]
    XMIN: float = RPARAMS[0]["xmin"]
    XMAX: float = RPARAMS[0]["xmax"]
    EX: float = RPARAMS[0]["ex"]
    N: int = RPARAMS[0]["n"]
    IS: int = RPARAMS[0]["isolv"]
    OM: float = RPARAMS[0]["omega"]
    EPSIL: float = RPARAMS[0]["epsil"]
    MAXIT: int = RPARAMS[0]["maxit"]
    RSDF: str = RPARAMS[0]["residf"]
    RSTF: str = RPARAMS[0]["rstout"]

    # delta_x
    dx: float = 0.

    # write out parameters and variables
    print(f"*** P1DS ***")
    # print(f"NX: {NX, type(NX)}, N: {N, type(N)}, NM: {NM, type(NM)}, FI[]: {FI,type(FI)}, DEN: {DEN, type(DEN)}, VEL: {VEL, type(VEL)}, DIF: {DIF, type(DIF)}, FI0:{FI0, type(FI0)}, FIN:{FIN, type(FIN)}, IC:{IC, type(IC)}, XMIN:{XMIN, type(XMIN)}, XMAX:{XMAX, type(XMAX)}, EX:{EX, type(EX)}, IS:{IS, type(IS)}, OM:{OM, type(OM)}, EPSIL:{EPSIL, type(EPSIL)}, MAXIT: {MAXIT, type(MAXIT)} \n")
    print(f"{PARAMS!r}")

    # out file name from STDIN
    FILOUT = args.output
    # Open files for write out data
    fout = open(FILOUT, "w")
    f_resd = open(RSDF, "w")
    f_rst = open(RSTF, "w")

    fout.write(f"# *** P1DS ***\n")
    fout.write(f"# NX: {NX, type(NX)}, PARAMS: {PARAMS}\n")

    # start of calculation
    NM = N - 1
    if (EX == 1.):
        dx = (XMAX - XMIN) / float(N - 1)
    else:
        dx = (XMAX - XMIN) * (1. - EX) / (1. - EX ** (N - 1))

    X[0] = XMIN

    for i in range(1, N):
        X[i] = X[i - 1] + dx
        dx = dx * EX

    # initialize fields
    for i in range(N+1):
        FI[i] = 0.

    FI[0] = FI0
    FI[NM] = FIN
    denvel = DEN * VEL
    ZERO = 0.

    # central difference convection approximation (CDS)
    for i in range(1, NM):
        if (IC == 1):
            AEC = denvel / (X[i + 1] - X[i - 1])
            AWC = -1.0 * AEC
        elif (IC == 2):
            AEC = min(denvel, ZERO) / (X[i + 1] - X[i])
            AWC = -1.0 * max(denvel, ZERO) / (X[i] - X[i - 1])
        # CD diffusion approximation
        DXR = 2.0 / (X[i + 1] - X[i - 1])
        AED = -1.0 * DIF * DXR / (X[i + 1] - X[i])
        AWD = -1.0 * DIF * DXR / (X[i] - X[i - 1])
        # assemble coefficient matrix
        AE[i] = AEC + AED
        AW[i] = AWC + AWD
        AP[i] = -1.0 * AW[i] - AE[i]
        Q[i] = 0.

    # boundary conditions
    Q[1] = Q[1] - AW[1] * FI[0]
    AW[1] = 0.0
    Q[NM-1] = Q[NM-1] - AE[NM-1] * FI[NM]
    AE[NM-1] = 0.

    # SOLVE
    if IS == 1:
        Jacobi()
    elif IS == 2:
        GaussSeidel()
    elif IS == 3:
        GSOR()
    elif IS == 4:
        TDMA()

    # calculate exact solution and error norm
    error = 0.0
    FIEX[0] = FI0
    FIEX[NM] = FIN
    peclet = denvel * (XMAX - XMIN) / DIF
    rx = 1.0 / (XMAX - XMIN)
    for i in range(1, NM):
        FIEX[i] = FI0 + (math.exp(peclet * X[i] * rx) - 1.0) / \
            (math.exp(peclet) - 1.0) * (FIN - FI0)
        error = error + abs(FIEX[i] - FI[i])
    error = error / float(N)

    # print the result
    print("\n\n")
    print(f"PECLET Number: PE = {peclet}")
    print(f"ERROR NORM = {error:12.6e}")
    fout.write("\n")
    fout.write(f"# PECLET Number: PE = {peclet}\n")
    fout.write(f"# ERROR NORM = {error:12.6e}\n")

    if IC == 1:
        fout.write(f"# CDS used for convection \n")
        print(f"CDS used for convection")
    if IC == 2:
        fout.write(f"# UDS used for convection \n")
        print(f"UDS used for convection")
    if IS == 1:
        fout.write(f"# JACOBI Solver \n")
        print(f"JACOBI Solver")
    if IS == 2:
        fout.write(f"# GAUSS-SEIDEL Solver \n")
        print(f"GAUß-SEIDEL Solver")
    if IS == 3:
        fout.write(f"# GSOR Solver \n")
        print(f"GSOR Solver")
    if IS == 4:
        fout.write(f"# TDMA Solver \n")
        print(f"TDMA Solver")

    fout.write(" \n")
    fout.write(f"X\t\tFI_EXACT\t\tFI\t\tERROR \n")
    fout.write(" \n")
    f_rst.write(f"X, FI_EXACT, FI, ERROR \n")

    print("\n")
    print(f"X\t\tFI_EXACT\t\tFI\t\tERROR")
    print("\n")

    # writeout comparison between calculated vs exact solution
    for i in range(0, N):
        fout.write(
            f"{X[i]:12.4e}, {FIEX[i]:14.6e}, {FI[i]:14.6e}, {FIEX[i] - FI[i]:14.6e}\n")
        print(
            f"{X[i]:12.4e}, {FIEX[i]:14.6e}, {FI[i]:14.6e}, {FIEX[i] - FI[i]:14.6e}")
        f_rst.write(
            f"{X[i]:12.4e}, {FIEX[i]:14.6e}, {FI[i]:14.6e}, {FIEX[i]-FI[i]:14.6e}\n"
        )
    # close output files
    fout.close()
    f_rst.close()
    f_resd.close()
    # end of main
    print(f"*** END of P1DS ***")
