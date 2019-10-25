#!/usr/bin/env python
# map_temp.py
# Map - Filter - Reduce
#

from __future__ import print_function


def main():
    # convert C -> F degree : F = 9/5 * C + 32
    temps = [("NP", 0, 0),("Istanbul", 22, 15), ("Berlin", 29, 14), ("Cairo", 36, 22),
             ("Buenos Aires", 19, 10), ("Los Angeles", 26, 15),
             ("Tokyo", 27, 12), ("New York", 28, 16), ("London", 22, 11),
             ("Beijing", 32, 21), ("Budapest", 15, 4), ("Caracas", 29, 15),
             ("Zagreb", 14, 3)]

    c_to_f = lambda data: (data[0], (9 / 5) * data[1] + 32, (9 / 5) * data[2] + 32)
    c_to_R = lambda data: (data[0], (9 / 5) * data[1] + 491.67, (9 / 5) * data[2] + 491.67)
    c_to_K = lambda data: (data[0], 273.15 + data[1], 273.15+data[2])

    c2F = list(map(c_to_f, temps))
    c2R = list(map(c_to_R, temps))
    c2K = list(map(c_to_K, temps))

    zipped = zip(temps, c2F, c2R, c2K)
    # print("Zipped HighT : ", [(z[:][0][0], z[:][0][1], z[:][1][1], z[:][2][1], z[:][3][1]) for z in zipped])

    [print(z[:][0][0],list(map(lambda d: (d[1]), z))) for z in zipped]

    # print("\nTemps [C] => \n", temps)
    # print("\nTemps[F]: -> ", list(map(c_to_f, temps)))
    # print("\nTemps[R]: -> ", list(map(c_to_R, temps)))
    # print("\nTemps[K]: -> ", list(map(c_to_K, temps)))


if __name__ == "__main__":
    main()
