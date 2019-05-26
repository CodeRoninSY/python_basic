#!/usr/bin/env python
# -*- coding: iso-8859-9 -*-
'''
subprocess_example.py

Author: CodeRoninSY
Date: <2019-05-19>
'''

import shlex
import subprocess
import click


cmd_line = input('Enter command >> ')
click.secho("cmd_line >> '%s'" % cmd_line, fg='green', bold=True)
args = shlex.split(cmd_line)
click.secho("args >> %s" % args, fg='green', bold=True)
p = subprocess.Popen(cmd_line, shell=True)

poll = subprocess.Popen.poll(p)
click.secho("poll >> %s" % poll, fg='yellow')
click.secho("pid >> %s" % p.pid, fg='white', bg='blue', bold=True)
click.secho("returncode >> %s" % p.returncode, fg='white', bg='blue', bold=True)
