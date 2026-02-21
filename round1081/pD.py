t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    edges = [[] for _ in range(n)]
    ans = [0] * n
    for i in range(n - 1):
        u, v = map(int, input().split())
        edges[u - 1].append(v - 1)
    sums = [0] * n
    scores = [0] * n
    depths = [0] * n
    heights = [0] * n
    def dfs(curr):
        sums[curr] += a[curr]
        for next in edges[curr]:
            depths[next] = depths[curr] + 1
            dfs(next)
            sums[curr] += sums[next]
            scores[curr] += scores[next] + sums[next]
            heights[curr] = max(heights[curr], heights[next] + 1)
        return
    dfs(0)
    
    diffs = [0] * n
    # print(heights)
    # print(sums)
    def dfs2(curr):
        diff = 0
        depth = depths[curr]
        longs = [0]

        for next in edges[curr]:
            delta = dfs2(next)
            diff = max(diff, delta)
            longs.append(heights[next] + 1)
        longs.sort()
        # print(longs)
        for next in edges[curr]:
            if heights[next] == longs[-1] - 1:
                diff = max(diff, longs[-2] * sums[next])
            else:
                diff = max(diff, longs[-1] * sums[next])
        # if diff != 0: print(diff)
        diffs[curr] = diff
        return diff
    dfs2(0)

    res = []
    for i in range(n):
        res.append(str(scores[i] + diffs[i]))
    print(" ".join(res))