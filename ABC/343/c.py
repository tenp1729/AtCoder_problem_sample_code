import math
from sys import exit
n = int(input())
t = int(math.pow(n, 1/3)+0.000001)
for i in reversed(range(t+1)):
    a = str(i**3)
    l = len(a)
    if all(a[j]==a[l-1-j]for j in range(l//2+1)):
        print(a)
        exit()
