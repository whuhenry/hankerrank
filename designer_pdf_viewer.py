"""
https://www.hackerrank.com/challenges/designer-pdf-viewer?h_r=next-challenge&h_v=zen
"""
#!/bin/python3

import sys

h = list(map(int, input().strip().split(' ')))
word = input().strip()

word_len = len(word)
height = 0
for char in word:
    if h[ord(char) - ord('a')] > height:
        height = h[ord(char) - ord('a')]
print(word_len * height)