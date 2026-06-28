t = int(input())
for _ in range(t):
    n = int(input())
    ans = 0
    for i in range(1, n + 1):
        ans += (n // i) ** 2
    print(ans)