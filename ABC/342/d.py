import math

n = int(input())
a = list(map(int, input().split()))
m = [0 for i in range(200001)]
z = a.count(0)
ans = (2*n-z-1)*z//2
for i in range(n):
    if a[i] <= 0:
        continue
    for j in reversed(range(1, math.floor(a[i]**0.5)+1)):
        if a[i] % (j**2) == 0:
            m[a[i]//(j**2)] += 1
            break
for i in range(200001):
    ans += m[i]*(m[i]-1)//2
print(ans)
