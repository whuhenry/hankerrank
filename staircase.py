"""
https://www.hackerrank.com/challenges/staircase?h_r=next-challenge&h_v=zen
"""

#!/bin/python3

import sys


n = int(input().strip())

for i in range(n):
    str_out = ""
    for j in range(n - i - 1):
        str_out += " "
    for j in range(i + 1):
        str_out +="#"
    print(str_out)
