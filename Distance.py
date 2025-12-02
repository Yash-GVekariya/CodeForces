from math import sqrt

def sqr(a):
    return a*a

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

print(sqrt(sqr(x2 - x1) + sqr(y2 - y1)))