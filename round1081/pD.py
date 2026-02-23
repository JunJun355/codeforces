# import sys
from collections import deque

# sys.setrecursionlimit(40000 )

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    adj = [[] for _ in range(n)]
    ans = [0] * n
    for i in range(n - 1):
        u, v = map(int, input().split())
        adj[u - 1].append(v - 1)
        adj[v - 1].append(u - 1)
    edges = [[] for _ in range(n)]
    to_search = deque()
    to_search.append(0)
    searched = set()
    while to_search:
        curr = to_search.popleft()
        searched.add(curr)
        for next in adj[curr]:
            if next in searched:
                continue
            edges[curr].append(next)
            to_search.append(next)

    sums = [0] * n
    scores = [0] * n
    depths = [0] * n
    heights = [0] * n
    # def dfs(curr):
    to_search = []
    to_search.append(0)
    i = 0
    while i < len(to_search):
        curr = to_search[i]
        sums[curr] += a[curr]
        for next in edges[curr]:
            depths[next] = depths[curr] + 1
            to_search.append(next)
        i += 1
    while to_search:
        curr = to_search.pop()
        for next in edges[curr]:
            sums[curr] += sums[next]
            scores[curr] += scores[next] + sums[next]
            heights[curr] = max(heights[curr], heights[next] + 1)
        # return
    # dfs(0)
    
    diffs = [0] * n
    # print(heights)
    # print(sums)
    to_search = [0]
    i = 0
    while i < len(to_search):
        curr = to_search[i]
        for next in edges[curr]:
            to_search.append(next)
        i += 1
    
    while to_search:
        curr = to_search.pop()
        longs = [0]
        for next in edges[curr]:
            diffs[curr] = max(diffs[curr], diffs[next])
            longs.append(heights[next] + 1)
        longs.sort()
        # print(longs)
        for next in edges[curr]:
            if heights[next] == longs[-1] - 1:
                diffs[curr] = max(diffs[curr], longs[-2] * sums[next])
            else:
                diffs[curr] = max(diffs[curr], longs[-1] * sums[next])
    # dfs2(0)

    res = []
    for i in range(n):
        res.append(str(scores[i] + diffs[i]))
    print(" ".join(res))