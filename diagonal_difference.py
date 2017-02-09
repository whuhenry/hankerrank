"""
https://www.hackerrank.com/challenges/diagonal-difference?h_r=next-challenge&h_v=zen
"""

#!/bin/python3

N = int(input().strip())
a = []
diff = 0
for a_i in range(N):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
    diff += a_t[a_i] - a_t[N - a_i - 1]

print(abs(diff))