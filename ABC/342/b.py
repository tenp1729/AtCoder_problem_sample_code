n = int(input())
p = list(map(int, input().split()))
q = int(input())
qu = [list(map(int, input().split()))for _ in range(q)]
dic = {p[i]: i for i in range(n)}
for i in range(q):
    if dic[qu[i][0]] < dic[qu[i][1]]:
        print(qu[i][0])
    else:
        print(qu[i][1])
