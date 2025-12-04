from math import sqrt

d = int(input())
sum = 0

for i in range(d):
    p1 = int(input())
    p2 = int(input())
    sum += (p2 - p1) ** 2

print(sqrt(sum))