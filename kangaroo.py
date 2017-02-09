"""
https://www.hackerrank.com/challenges/kangaroo?h_r=next-challenge&h_v=zen
"""
#!/bin/python3

import sys


x1,v1,x2,v2 = input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]

if v1 == v2:
    if x1 == x2:
        print('YES')
    else:
        print('NO')
else:
    n = (x2 - x1) / (v1 - v2)
    mol = (x2 - x1) % (v1 - v2)
    if n >= 0 and mol == 0:
        print('YES')
    else:
        print("NO")
