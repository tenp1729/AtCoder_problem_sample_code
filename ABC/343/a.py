a, b = map(int, input().split())
ans = 0
for i in range(10):
    if a + b != i:
        ans = i
        break
print(ans)
