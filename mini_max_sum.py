"""
https://www.hackerrank.com/challenges/mini-max-sum
"""
#!/bin/python

import sys


a,b,c,d,e = input().strip().split(' ')
input_array = [int(a),int(b),int(c),int(d),int(e)]
min = 1000000000
max = 0
sum_array = 0
for num in input_array:
    if num > max:
        max = num
    if num < min:
        min = num
    sum_array += num
print(sum_array - max, sum_array - min)
