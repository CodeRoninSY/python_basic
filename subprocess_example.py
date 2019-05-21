#!/usr/bin/env python
# -*- coding: windows-1252 -*-
'''

subprocess_example.py

Author: CodeRoninSY
Date: <2019-05-19>

'''

import shlex
import subprocess
import click


cmd_line = input('Enter command >> ')
args = shlex.split(cmd_line)
click.secho("args >> %s" % args, fg='green', bold=True)
p = subprocess.Popen(args)

poll = subprocess.Popen.poll(p)
click.secho("poll >> %s" % poll, fg='yellow')
click.secho("pid >> %s" % p.pid, fg='white', bg='blue', bold=True)
print(p.returncode)
