#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
argparse_cylinder.py

Youtube: Johnny Metz, Argparse

CodeRoninSY
<2019-05-29>
'''

import math
import argparse

parser = argparse.ArgumentParser(description='Calculate volume of a cylinder')
parser.add_argument(
    '-r', '--radius', type=float, nargs='?', metavar='', help='Radius of cylinder', default=1.0)
parser.add_argument(
    '-l', '--height', type=float, nargs='?', metavar='', help='Height of cylinder', default=1.0)
group = parser.add_mutually_exclusive_group()
group.add_argument('-q', '--quiet', action='store_true', help='print quiet')
group.add_argument('-v', '--verbose', action='store_true', help='print verbose')
args = parser.parse_args()


def cylinder_vol(radius=None, height=None):
    ''' cylinder_volume '''
    if radius < 0:
        msg = "%f is not positive" % radius
        raise argparse.ArgumentTypeError(msg)
    vol = (math.pi) * (radius ** 2) * height
    return vol


if __name__ == '__main__':
    ''' MAIN driver '''
    vol = cylinder_vol(args.radius, args.height)
    if args.quiet:
        print(vol)
    elif args.verbose:
        print("Volume of a cylinder with radius %s and height %s is %s" % \
            (args.radius, args.height, vol))
    else:
        print("Volume of cylinder = %s" % vol)
