t = int(input())
for _ in range(t):
    n, h, k = map(int, input().split())
    arr = list(map(int, input().split()))
    s = sum(arr)
    ans = h // s * (len(arr) + k) - k
    h = h % s
    if h == 0:
        print(ans)
        continue
    ans += k

    bot, top = 1, n + 1
    while bot < top:
        mid = (bot + top) // 2
        su = sum(arr[:mid])
        mi = min(arr[:mid])
        ma = max(arr[mid:] + [mi])
        su = su - mi + ma
        if su >= h:
            top = mid
        else:
            bot = mid + 1

    # ms = [n - 1]
    # for i in range(n - 2, 0, -1):
    #     if arr[i] > arr[ms[-1]]:
    #         ms.append(i)
    
    # dp = [[0] * (n + 1) for _ in range(2)]
    # dp[0][0] = h
    # dp[1][0] = h
    # for i in range(1, n + 1):
    #     dp[0][i] = max(0, dp[0][i - 1] - arr[i - 1])
    # for i in range(1, n + 1):
    #     if i > ms[-1]: ms.pop()
    #     dp[1][i] = max(0, min(dp[1][i - 1] - arr[i - 1], dp[0][i - 1] - ms))


    print(ans + bot)