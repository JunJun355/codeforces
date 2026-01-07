from collections import defaultdict
# from time import sleep
# sleep(1)
t = int(input())
for _ in range(t):
    n = int(input())
    graph = defaultdict(lambda:[])
    for _ in range(n - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    layersizes = defaultdict(lambda:0)
    depths = defaultdict(lambda:-1)
    depths[1] = 0
    to_search = [1]
    searched = set()
    while to_search:
        curr = to_search.pop()
        searched.add(curr)
        for next in graph[curr]:
            if next in searched:
                continue
            depths[next] = depths[curr] + 1
            to_search.append(next)
        layersizes[depths[curr]] += 1
    ans = max(layersizes.values())
    ans = max(ans, len(graph[1]) + 1)
    for i in range(2, n + 1):
        ans = max(ans, len(graph[i]))
    print("     ", ans)
        