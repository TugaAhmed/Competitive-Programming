# https://www.hackerrank.com/challenges/python-power-mod-power/problem?isFullScreen=true

from math import pow

a = int(input())
b = int(input())
m = int(input())

print(a ** b)
print(a ** b % m)
