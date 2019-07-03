#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
p1dus_v1.py

Synopsis: Unsteady 1D convection-diffusion equation with Dirichlet boundary conditions on both ends.
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
    1. param_p1dus.json   = parameters json config file for parameters used in code

DATA::
    DEN         : Density
    VEL         : Velocity
    DIF         : Diffusion
    DT          : Delta_t
    NTMAX       : Max Number of time step
    NTPR        : print-out period
    FI0         : fi_0
    FIN         : fi_N
    IC          : convection term (1 - CDS, 2 - UDS)
    IT          : time discretization (1 -> EE, 2 -> IE, 3 -> CN, 4 -> I3L)
    IS          : Solver ( 1-> TDMA)
    MAXIT       : max iteration no (not used)
    EPSIL        : Epsilon

Output Data/File:
    1. fileout          = output written to "fileout" via -o, --output option

Methods::
    1. TDMA()         : Tridiagonal Matrix Algorithm

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
        return f"TITLE:{self.title}, DENS={self.den}, VELO={self.vel}, DIFF={self.dif}, DT={self.dt}, NTMAX={self.ntmax}, NTPR={self.ntpr}, FI0={self.fi0}, FIN={self.fin}, SCHEME={self.ic}, IT={self.it}, XMIN={self.xmin}, XMAX={self.xmax}, EXPAN={self.ex}, N={self.n}, ISOLV={self.isolv}, OMEGA={self.omega}, EPSILON={self.epsil}, MAXIT={self.maxit}, ResidFile={self.residf}, ResultFile={self.rstout}"

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
# @timeit
def TDMA():
    """ TriDiagonal Matrix Algorithm Subroutine
    Initialization by zero assumed!
    UPR(I) = reciprocal value of UP(I)
    QS(I) = modified source term
    """
    bpr: np.longdouble = np.zeros(NX)
    v: np.longdouble = np.zeros(NX)

    # forward substitution
    for i in range(1, NM):
        bpr[i] = 1.0 / (AP[i] - AW[i] * AE[i - 1] * bpr[i - 1])
        v[i] = Q[i] - AW[i] * v[i - 1] * bpr[i - 1]
    # backward substitution
    for i in range(NM-1, 1, -1):
        FI[i] = (v[i] - AE[i] * FI[i+1]) * bpr[i]


# ----------------------------------------------------------------------
# MAIN Driver
if __name__ == "__main__":
    ''' MAIN driver '''
    # CLI argument parser
    parser = argparse.ArgumentParser(
        description="P1DUS Unsteady 1-D convection-diffusion equation solver.")
    parser.add_argument('-o', '--output', type=str,
                        default='p1dus.out', help="fileout output file.")
    parser.add_argument('-p', '--parameter', type=int,
                        default=10001, help="NX parameter for max array lengths.")
    parser.add_argument('-i', '--input', nargs='?', type=str,
                        default='param_p1dus.json', help="parameter json file for input.")
    args = parser.parse_args()

    # clear screen
    if platform.system() == "Windows":
        subprocess.Popen("cls", shell=True).communicate()
    elif platform.system() == "Linux":
        subprocess.Popen("clear", shell=True).communicate()

    print(f"\n\n<*  P.1.D.U.S  *>\n\n")

    print(f"{__doc__}")
    print(f"Author: {__author__}")
    print(f"Version: {__version__}")
    print(f"Date: {__date__}")
    # print("\n\n*** P 1 D U S ***\n\n")

    # parameter NX
    NX: int = args.parameter
    # in/out filename
    FILOUT: str = args.output
    FILIN: str = args.input

    PARAMS = getParams(FILIN)
    RPARAMS = getParams(FILIN, raw=True)

    # pprint(PARAMS, indent=4)
    # pprint(RPARAMS, indent=4)

    # COMMON/var/ block
    N: np.int32 = 0
    NM: np.int32 = 0
    FI: np.longdouble = np.zeros(NX)
    AE: np.longdouble = np.zeros(NX)
    AW: np.longdouble = np.zeros(NX)
    AP: np.longdouble = np.zeros(NX)
    Q: np.longdouble = np.zeros(NX)
    X: np.longdouble = np.zeros(NX)

    FIEX: np.longdouble = np.zeros(NX)
    FIOO: np.longdouble = np.zeros(NX)
    FIO: np.longdouble = np.zeros(NX)

    np.array(FI, dtype=np.longdouble, ndmin=1)
    np.array(AE, dtype=np.longdouble, ndmin=1)
    np.array(AW, dtype=np.longdouble, ndmin=1)
    np.array(AP, dtype=np.longdouble, ndmin=1)
    np.array(Q, dtype=np.longdouble, ndmin=1)
    np.array(X, dtype=np.longdouble, ndmin=1)
    np.array(FIEX, dtype=np.longdouble, ndmin=1)

    # ... input settings
    DEN: np.longdouble = RPARAMS[0]["den"]
    VEL: np.longdouble = RPARAMS[0]["vel"]
    DIF: np.longdouble = RPARAMS[0]["dif"]
    DT: np.longdouble = RPARAMS[0]["dt"]
    NTMAX: np.int32 = RPARAMS[0]["ntmax"]
    NTPR: np.int32 = RPARAMS[0]["ntpr"]
    FI0: np.longdouble = RPARAMS[0]["fi0"]
    FIN: np.longdouble = RPARAMS[0]["fin"]
    IC: np.int8 = RPARAMS[0]["ic"]
    IT: np.int8 = RPARAMS[0]["it"]
    XMIN: np.longdouble = RPARAMS[0]["xmin"]
    XMAX: np.longdouble = RPARAMS[0]["xmax"]
    EX: np.longdouble = RPARAMS[0]["ex"]
    N: np.int32 = RPARAMS[0]["n"]
    IS: np.int8 = RPARAMS[0]["isolv"]
    OM: np.longdouble = RPARAMS[0]["omega"]
    EPSIL: np.longdouble = RPARAMS[0]["epsil"]
    MAXIT: np.int32 = RPARAMS[0]["maxit"]
    RSDF: str = RPARAMS[0]["residf"]
    RSTF: str = RPARAMS[0]["rstout"]

    # ... global data
    DENVEL: np.longdouble = 0.0
    ZERO: np.longdouble = 0.0
    TTIME: np.longdouble = 0.0
    DDTR: np.longdouble = 0.0
    BETA: np.longdouble = 0.0

    dx: np.longdouble = 0.0
    DXR: np.longdouble = 0.0
    pe: np.longdouble = 0.0
    dfac: np.longdouble = 0.0
    cfac: np.longdouble = 0.0

    tstrt: np.float32 = 0.0
    tend: np.float32 = 0.0

    # ... clock started
    tsrt = time.clock()

    # ... write out parameters and variables
    print(f"\n*** P1DUS ***\n")
    print(f"{PARAMS!r}")

    # out file name from STDIN
    FILOUT = args.output
    # Open files for write out data
    fout = open(FILOUT, "w")
    f_resd = open(RSDF, "w")
    f_rst = open(RSTF, "w")

    fout.write(f"# *** P1DUS ***\n")
    fout.write(f"# NX: {NX, type(NX)}, PARAMS: {PARAMS}\n")

    # start of calculation
    NM = N - 1
    if (EX == 1.):
        dx = (XMAX - XMIN) / float(N - 1)
    else:
        dx = (XMAX - XMIN) * (1. - EX) / (1. - EX ** (N - 1))

    X[0] = XMIN

    for i in np.arange(1, N):
        X[i] = X[i - 1] + dx
        dx = dx * EX

    # initialize solution, set boundary values
    for i in np.arange(N+1):
        FI[i] = 0.0
        FIO[i] = 0.0

    FI[0] = FI0
    FI[NM] = FIN
    DENVEL = DEN * VEL
    ZERO = 0.0

    # ... start time loop (beta=0. for the first step & 3-level scheme)
    TTIME = 0.0
    DDTR = DEN / DT
    BETA = 0.0

    for nt in np.arange(1, NTMAX + 1):
        TTIME += DT
        # ... shift solutions to older levels
        for i in np.arange(N):
            FIOO[i] = FIO[i]
            FIO[i] = FI[i]
        FI[0] = FI0
        FI[NM] = FIN

        # ... discretize convection term using UDS
        if (IC == 1):
            for i in np.arange(1, NM):
                DXR = 1.0 / (X[i + 1] - X[i - 1])
                AE[i] = DENVEL * DXR
                AW[i] = -1.0 * DENVEL * DXR
            # ... discretize convection term using CDS (no deferred correction)
        elif (IC == 2):
            for i in np.arange(1, NM):
                AE[i] = min(DENVEL, ZERO) / (X[i + 1] - X[i])
                AW[i] = -1.0 * max(DENVEL, ZERO) / (X[i] - X[i - 1])

        # ... discretize diffusion term (CDS)
        for i in np.arange(1, NM):
            DXR = 1.0 / (X[i + 1] - X[i - 1])
            AE[i] = AE[i] - DIF * DXR / (X[i + 1] - X[i])
            AW[i] = AW[i] - DIF * DXR / (X[i] - X[i - 1])
            Q[i] = 0.0
        # ... time discretization -> explicit euler
        if (IT == 1):
            for i in np.arange(1, NM):
                Q[i] = Q[i] - AE[i] * FIO[i + 1] - AW[i] * FIO[i - 1] + (DDTR + AE[i] + AW[i]) * FIO[i]
                AP[i] = DDTR
                AE[i] = 0.0
                AW[i] = 0.0
        # ... time discretization -> implicit euler
        elif (IT == 2):
            for i in np.arange(1, NM):
                Q[i] = Q[i] + DDTR * FIO[i]
                AP[i] = DDTR - AE[i] - AW[i]
        # ... time discretization -> crank-nicholson
        elif (IT == 3):
            for i in np.arange(1, NM):
                AE[i] = 0.5 * AE[i]
                AW[i] = 0.5 * AW[i]
                Q[i] = Q[i] - AE[i] * FIO[i + 1] - AW[i] * FIO[i - 1] + (DDTR + AE[i] + AW[i]) * FIO[i]
                AP[i] = DDTR - AE[i] - AW[i]
        # ... time discretization -> implicit 3-level
        elif (IT == 4):
            for i in np.arange(1, NM):
                Q[i] = Q[i] + DDTR * ((1.0 + BETA) * FIO[i] - 0.5 * BETA * FIOO[i])
                AP[i] = DDTR * (1.0 + 0.5 * BETA) - AE[i] - AW[i]

        # .. adjust boundary source & coeff.
        Q[1] = Q[1] - AW[1] * FI[0]
        AW[1] = 0.0
        Q[NM - 1] = Q[NM - 1] - AW[NM - 1] * FI[NM]
        AE[NM - 1] = 0.0
        # ... solve equation system
        if (IS == 1):
            TDMA()

        # ... print the result (every ntpr-th time step)
        if (nt % NTPR == 0):
            pe = DEN * VEL * (XMAX - XMIN) / DIF
            dfac = DIF * DT / (DEN * dx ** 2)
            cfac = VEL * DT / dx

            print(f"\n")
            print(f"     PECLET NUMBER: PE = {pe}")
            print(f"  DIFFUSION NUMBER: D  = {dfac:.2f}")
            print(f"    COURANT NUMBER: Co = {cfac:.2f}")
            print(f"         TIME STEP: DT = {DT:.3f}")
            print(f"              TIME: T  = {TTIME:.3f}")

            fout.write(f"\n")
            fout.write(f"     PECLET NUMBER: PE = {pe}\n")
            fout.write(f"  DIFFUSION NUMBER: D  = {dfac:.2f}\n")
            fout.write(f"    COURANT NUMBER: Co = {cfac:.2f}\n")
            fout.write(f"         TIME STEP: DT = {DT:.3f}\n")
            fout.write(f"              TIME: T  = {TTIME:.3f}\n")

            if (IC == 2):
                print(f"   UPWIND CONVECTION ")
                fout.write(f"   UPWIND CONVECTION \n")
            if (IC == 1):
                print(f"   CDS CONVECTION ")
                fout.write(f"   CDS CONVECTION \n")
            if (IT == 1):
                print(f"   EXPLICIT EULER TIME DISCR. ")
                fout.write(f"   EXPLICIT EULER TIME DISCR. \n")
            if (IT == 2):
                print(f"   IMPLICIT EULER TIME DISCR. ")
                fout.write(f"   IMPLICIT EULER TIME DISCR. \n")
            if (IT == 3):
                print(f"   CRANK-NICHOLSON TIME DISCR. ")
                fout.write(f"   CRANK-NICHOLSON TIME DISCR. \n")
            if (IT == 4):
                print(f"   IMPLICIT 3 LEVEL TIME DISCR. ")
                fout.write(f"   IMPLICIT 3 LEVEL TIME DISCR. \n")

            print(f"\n")
            print(f"       X           FI ")

            fout.write(f"\n")
            fout.write(f"       X           FI \n")
            for i in np.arange(0, N):
                print(f"{X[i]:16.8e},{FI[i]:16.8e}")
                fout.write(f"{X[i]:16.8e},{FI[i]:16.8e}\n")
            fout.write(f"# ENDT = {TTIME:.3f}\n\n")

        # ... set BETA=1.0 for subsequent time steps
        BETA = 1.0

    # ... do end
    tend = time.clock()
    print(f"\n\nCPU time = {tend - tstrt:.3f} sec.\n")

    # close output files
    fout.close()
    f_rst.close()
    f_resd.close()
    # end of main
    print(f"*** END of P1DUS ***")
