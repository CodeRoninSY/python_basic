#!/usr/bin/env python
# heredoc_example.py
# Copyright (c) 2020
# Author: CodeRoninSY


text="""{name}
was
{place}"""

print(text.format(name='Louis', place='here'))

filedb = "file"
rest1 = "lm9k_hptr_2D_B2DDR_"

apdl = """/batch
! B2 DDR PG41F v1.48
!
! For initial run, start with clean DB from preload
/resume,{filedb},db,

! For restart from any cycle/tp
/sys,gzip -df {rest1}.db.gz
/sys,gzip -df {rest1}.emat.gz
/sys,gzip -df {rest1}.esav.gz
/sys,gzip -f {rest1}.rst.gz

fini
/eof

"""

class APDLWriter(object):
    """ APDLWriter """
    def __init__(self, filedb, rest1) -> None:
        self.filedb = filedb
        self.rest1 = rest1

    def _writeInp(self, inpfile, heredoc):
        with open(inpfile, mode='w') as f:
            f.write(heredoc.format(filedb=self.filedb,
                    rest1=self.rest1))


print(apdl.format(filedb=filedb, rest1=rest1))

aw = APDLWriter("file", "lm9k__")
aw._writeInp("inpfile.inp", apdl)

aw2 = APDLWriter("f_new", "lm9k___")
aw2._writeInp("inpfile2.mac", apdl)