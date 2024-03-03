n, t = map(int, input().split())
player = [0 for i in range(n)]
dic = {0: n}
ans = 1
for i in range(t):
    pl, point = map(int, input().split())
    pp = player[pl-1]
    player[pl-1] += point
    if dic[pp] <= 1:
        del dic[pp]
        ans -= 1
    else:
        dic[pp] -= 1
    pp += point
    if pp in dic:
        dic[pp] += 1
    else:
        dic[pp] = 1
        ans += 1
    print(ans)
