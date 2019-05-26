# !/usr/bin/env python3
'''
For use within vim:
    : vnoremap <silent> <leader>[ :w ! python3<CR>
    : nnoremap <silent> <leader>[[ :%w ! python3<CR>
    : vnoremap <silent> <leader>] :Tyank<CR>
    " : vnoremap <silent> <leader>] :Twrite bottom<CR>
'''

from builtins import print as _print

__title__ = 'Python Generators'
__author__ = 'CodeRoninSY'
__github__ = 'CodeRoninSY'



def print(*args, **kwargs):
    ''' redefine/overload print function '''
    _print(*args, **kwargs)
    _print(f'@{__github__}'.rjust(80, ' '))


def add1(x, y):
    return x + y

add2 = lambda x, y: x + y

print(f'add1: {add1(1, 2)}')
print(f'add2: {add2(1, 2)}')

class Adder():
    def __init__(self, z=0):
        self.z = z
    def __call__(self, x, y):
        self.z += 1
        return x + y + self.z


add3 = Adder()

print(f'add3: {add3(1, 2)}')
print(f'add3: {add3(1, 2)}')
print(f'add3: {add3(1, 2)}')
