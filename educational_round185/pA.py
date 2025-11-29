t = int(input())
for _ in range(t):
    n = int(input())
    ans = 1
    if n  > 1:
        ans = max(ans, 3 * n ** 2 - 1 - n)
    if n > 2:
        ans = max([ans, 4 * n ** 2 - n - 4, 5 * n ** 2 - 5 * n - 5])
    print(ans)