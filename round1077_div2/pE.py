from heapq import *
from collections import defaultdict
from time import sleep

def solve():
    n, m = map(int, input().split())
    edges = []
    adj = defaultdict(list)
    for i in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        edges.append((u, v))
        adj[u].append(v)
    edges.sort()
    skips_above = [0] * (n)
    heap = []
    for i in range(n):
        while heap and heap[0] <= i:
            heappop(heap)
        skips_above[i] = len(heap)
        for next in adj[i]:
            heappush(heap, next)
    print(skips_above)

    ans = [0] * n
    dist = [float('inf')] * n
    stuff = []
    for i in range(n - 1, -1, -1):
        if skips_above[i] == 0:
            dist[i] = 0
            stuff.sort()
            pd = float('inf')
            pn = len(stuff)
            while stuff:
                d, ind = stuff.pop()
                if d != pd:
                    pd = d
                    pn = len(stuff)

                ans[ind] += (i + pn) * d
        else:
            dist[i] = dist[i + 1] # yeah yeah
            for next in adj[i]:
                dist[i] = min(dist[i], dist[next])
        stuff.append((dist[i], i))
    print(ans)
        


t = int(input())
sleep(0.1)
for _ in range(t):
    solve()