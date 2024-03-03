n = int(input())
for i in range(n):
    a = list(map(int, input().split()))
    ans = [i+1 for i in range(n) if a[i] == 1]
    print(*ans)
