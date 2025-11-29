t = int(input())
for _ in range(t):
    n, k = [int(c) for c in input().split()]
    q = [int(c) for c in input().split()]
    r = [int(c) for c in input().split()]
    q.sort()
    r.sort()
    bot, top = -1, n - 1
    ans = 0
    for i in range(n):
        if top == -1:
            break
        while bot < top:
            mid = (bot + top + 1) // 2
            if q[mid] * (r[i] + 1) + r[i] <= k:
                bot = mid
            else:
                top = mid - 1
        if top >= 0:
            ans += 1
        top -= 1
        bot = -1
    print(ans)
