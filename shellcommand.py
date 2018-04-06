#!/usr/bin/python -u 
# -*- coding: utf-8 -*-

# Warning : this script is a huge security breach in WARP10 system and must not be here in a shared environment
#
# This scripts take a list of commands, or command + args, execute it in a shell, return a list of each stdout line.
# Command error is simply handled with "Shell error, cannot execute your command" message
#
# WARP10 examples:
#
# if list contains only one string, it will be executed in shell mode.
# [ 'ps aux | grep "^warp" ' ] ->PICKLE ->HEX 'shellcommand.py' CALL HEX-> PICKLE->
#
# if list contains multiple strings, they will be executed as program arg1... argN
# [ 'ls' '-1'  '/etc'  '/home' ] ->PICKLE ->HEX 'shellcommand.py' CALL HEX-> PICKLE->
#

import pickle
import sys
import subprocess

#
# Output the maximum number of instances of this 'callable' to spawn
# The absolute maximum is set in the configuration file via 'warpscript.call.maxcapacity'
#
print 10

# wait for input
line = sys.stdin.readline()
# remove leading and trailing spaces
line = line.strip()
# rebuild the input list from hex string
InputArgs = pickle.loads(line.decode("hex"))

try:
    # use subprocess and get shell output
    shell_exec = ( 1 == len(InputArgs))
    out = subprocess.check_output(InputArgs, shell=shell_exec)
except:
    # error must begin with a space to raise an exception in WARP10
    print " Shell%20error%2C%20cannot%20execute%20your%20command"

# build a list of each output line
out_list = out.splitlines()

# output is pickled and dumped as hex
output = pickle.dumps(out_list)
print output.encode('hex')
