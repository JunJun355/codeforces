from collections import defaultdict, deque
from heapq import *

def solve():
    n, m = map(int, input().split())
    edges = defaultdict(list)
    for i in range(m):
        i, j = map(int, input().split())
        edges[i - 1].append(j - 1)
        edges[j - 1].append(i - 1)
    ans = 0
    side = [-1] * n
    for i in range(n):
        if side[i] != -1: continue
        side[i] = 0
        bipartite = True
        sources = 0
        dests = 0
        stack = [i]
        while stack:
            curr = stack.pop()
            if side[curr] == 0: sources += 1
            else: dests += 1
            for next in edges[curr]:
                if side[next] == side[curr]:
                    bipartite = False
                if side[next] != -1: continue
                side[next] = 1 - side[curr]
                stack.append(next)
        if bipartite: ans += max(sources, dests)
    print(ans)
    

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()