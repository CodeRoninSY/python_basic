#!/usr/bin/env python
# heredoc_example.py
# Copyright (c) 2020
# Author: CodeRoninSY

# file.db & restart file basename
f1 = "file"
r1 = "EngCodeName_hptr_2D_B3DDR_"
IST = 1
IEND = 126
i0_ = 12

apdl = """/batch
! EngCodeName B3 DDR MissionCase41F v0.01
!
! For initial run, start with clean DB from preload
/resume,{filedb},db,

! For restart from any cycle/tp
/sys,gzip -df {restf}.db.gz
/sys,gzip -df {restf}.emat.gz
/sys,gzip -df {restf}.esav.gz
/sys,gzip -df {restf}.rst.gz

*do,ii,1,5

    *do,i0_,{ist},{iend}+1,1


    !i0_={i0_}

    *end
*end

fini
/eof

"""


PARAMS = {
    'P3r_': 123.45,
    'P4r_': 111.22,
    'P25r_': 33.333,
    'P42r_': 44.44,
    }


gasdoc = """
{}={}"""


class APDLWriter(object):
    """ APDLWriter """
    def __init__(self, filedb, restf, ist, iend, i0_):
        self.filedb     = filedb
        self.restf      = restf
        self.ist        = ist
        self.iend       = iend
        self.i0_        = i0_

    def __repr__(self):
        return {self.filedb}, {self.restf}

    def _writeInput(self, inpfile, heredoc):
        with open(inpfile, mode='w') as f:
            f.write(heredoc.format(filedb=self.filedb,
                    restf=self.restf, ist=self.ist,
                    iend=self.iend, i0_=self.i0_))

    def _gasload(self, filename, gasdoc, **dict):
        with open(filename, 'a') as f:
            f.write("!**********************\n")
            f.write(":Gasloads_\n")
            for k, v in dict.items():
                f.write(gasdoc.format(k,v))
                # print("{k}={v}")
            f.write("\n\nfinish\n")
            f.write("/eof\n")



# print(apdl.format(filedb=f1, restf=r1))

aw = APDLWriter("file", "eng_3D__", IST, IEND, i0_)
aw._writeInput("inpfile.inp", apdl)

aw2 = APDLWriter("f_new", "nhp_3D__", IST, IEND, i0_)
aw2._writeInput("inpfile2.mac", apdl)
aw2._gasload("inpfile2.mac", gasdoc, **PARAMS)

print(aw2.__repr__())
