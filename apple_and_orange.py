#!/bin/python3

import sys


s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]

apple_count = 0
for fruit in apple:
    loc = a + fruit
    if loc >= s and loc <= t:
        apple_count += 1

orange_count = 0
for fruit in orange:
    loc = b + fruit
    if loc >= s and loc <= t:
        orange_count += 1

print(apple_count)
print(orange_count)