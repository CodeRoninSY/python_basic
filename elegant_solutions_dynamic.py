#!/usr/bin/env python
# -*- coding: windows-1252 -*-
'''
elegant_solutions_dynamic.py

= command line tools with dynamic commands =
From Nina Zakharenko - Elegant solutions for everyday python problems
PyCon 2018

Dev: CodeRoninSY
Date: <2019-05-13>

Note:
    1. added multi args for class methods

'''


class Operations:
    ''' Operations class '''
    def say_hi(self, *name):
        print('Hello,', " ".join(*name))

    def say_bye(self, *name):
        print('Goodbye,', " ".join(*name))

    def default(self, arg):
        print('This operation is not supported.')


if __name__ == '__main__':
    ''' main() '''
    operations = Operations()
    # let's assume error handling
    command, *argument = input('$>> ').split()
    getattr(operations, command, operations.default)(argument)
