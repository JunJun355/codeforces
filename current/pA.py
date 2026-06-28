t = int(input())
for _ in range(t):
    n, c = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    first = 0
    for i in range(n):
        if a[i] < b[i]:
            first = float('inf')
            break
        first += a[i] - b[i]

    second = c
    a.sort()
    b.sort()
    for i in range(n):
        if a[i] < b[i]:
            second = float('inf')
            break
        second += a[i] - b[i]

    ans = min(first, second)
    if ans > 1e9: print(-1)
    else: print(ans)