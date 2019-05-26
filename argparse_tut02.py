#!/usr/bin/env python
''' argparse_tut02.py
Command line programs in python - CLA
<2019-04-27> CodeRoninSY
'''

import argparse

def main():
    ''' main() '''
    parser = argparse.ArgumentParser()
    parser.add_argument("square", help="display a square of a given number",
                        type=int)
    parser.add_argument("-v", "--verbose", type=int, choices=[0, 1, 2],
                        help="increase output verbosity")
    args = parser.parse_args()
    answer = args.square**2
    if args.verbose == 2:
        print("the square of {} equals {}".format(args.square, answer))
    elif args.verbose == 1:
        print("{}^2 == {}".format(args.square, answer))
    else:
        print(answer)


if __name__ == "__main__":
    main()
