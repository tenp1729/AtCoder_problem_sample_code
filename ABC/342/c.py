n = int(input())
s = list(input())
q = int(input())
query = [list(map(str, input().split())) for _ in range(q)]
letter = [chr(i + 97) for i in range(26)]
for i in range(q):
    x = query[i][0]
    y = query[i][1]
    for j in range(26):
        if letter[j] == x:
            letter[j] = y
dic = {chr(i + 97): letter[i] for i in range(26)}
for i in range(n):
    s[i] = dic[s[i]]
ans = "".join(s)
print(ans)
