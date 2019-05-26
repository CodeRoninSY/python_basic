#!/usr/bin/env python3
'''
For use within vim:
    : vnoremap <silent> <leader>[ :w ! python3<CR>
    : nnoremap <silent> <leader>[[ :%w ! python3<CR>
    : vnoremap <silent> <leader>] :Tyank<CR>
    " : vnoremap <silent> <leader>] :Twrite bottom<CR>
'''

__title__ = 'Python Generators'
__author__ = 'CodeRoninSY'
__github__ = 'CodeRoninSY'


from builtins import print as _print
# redefine/overload print function
def print(*args, **kwargs):
    _print(*args, **kwargs)
    _print(f'@{__github__}'.rjust(80, ' '))


if __name__ == '__main__':
    print(__title__)
    print(__author__)
    print(__github__)
