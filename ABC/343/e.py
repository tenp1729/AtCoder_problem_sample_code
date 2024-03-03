import itertools
from sys import exit

def mr(s, t):
    h = max(s,t)
    l = min(s,t)
    return max(l+7-h, 0)


def mlr(s):
    h = max(s)
    l = min(s)
    return max(l+7-h, 0)


v = list(map(int, input().split()))
lst = list(itertools.product(list(range(-1,8)), repeat=6))
for a2,b2,c2,a3,b3,c3 in lst:
    p = [[0,0,0],[a2,b2,c2,],[a3,b3,c3]]
    a = [0,a2,a3]
    b = [0,b2,b3]
    c = [0,c2,c3]
    v3 = max(0, mlr(a)*mlr(b)*mlr(c))
    if v[2] != v3:
        continue
    v2 = -3 * v3
    for i in range(2):
        for j in range(i+1,3):
            vx = mr(a[i],a[j])*mr(b[i],b[j])*mr(c[i],c[j])
            v2 += max(0, mr(a[i],a[j])*mr(b[i],b[j])*mr(c[i],c[j]))
    if v2 != v[1] or 1029 - 2 * v2 - 3 * v3 != v[0]:
        continue
    print("Yes")
    ans = p[0]+p[1]+p[2]
    print(*ans)
    exit()
print("No")
