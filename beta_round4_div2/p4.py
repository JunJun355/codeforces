def main():
    n, w, h = [int(c) for c in input().split()]
    envelopes = []
    for i in range(n):
        w1, h1 = [int(c) for c in input().split()]
        envelopes.append([i, w1, h1])
    envelopes.sort(key=lambda x : (x[1], -x[2], x[0]))
    # print(envelopes)
    dp = [float('inf')] * 5001
    which = [-1] * 5001
    prev = [-1] * 5000
    dp[0] = h
    for env in envelopes:
        i, w1, h1 = env
        if w1 <= w: continue
        bot, top = -1, 5000
        while bot < top:
            mid = (bot + top + 1) // 2
            if dp[mid] < h1:
                bot = mid
            else:
                top = mid - 1
        if bot >= 0 and dp[bot + 1] > h1:
            dp[bot + 1] = h1
            which[bot + 1] = i
            prev[i] = which[bot]
    res = []
    for i in range(5000, -1, -1):
        if which[i] >= 0:
            res.append(which[i])
            break
    if not res:
        print(0)
        return
    while prev[res[-1]] != -1:
        res.append(prev[res[-1]])
    print(len(res))
    print(" ".join([str(c + 1) for c in res[::-1]]))
        


if __name__ == '__main__':
    main()