#!/bin/python3

import sys


time = input().strip()
hh = int(time[0:2])
mm = int(time[3:5])
ss = int(time[6:8])
other = time[8:]
if(other == 'PM'):
    if hh != 12:
        hh += 12
else:
    if hh == 12:
        hh = 0

print("%02d:%02d:%02d" % (hh, mm, ss))