# from heapq import *
import heapq


n, m = map(int, input().split())
edges = [[float('inf')] * n for _ in range(n)]

graph = [[] for _ in range(n + 1)]
    
# Parse the edges
idx = 2
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))
    idx += 3
    
# Initialize shortest distances to infinity
distances = {i: float('inf') for i in range(1, n + 1)}
distances[1] = 0

# Priority queue stores tuples of (current_distance, node)
pq = [(0, 1)]

while pq:
    current_dist, u = heapq.heappop(pq)
    
    # Skip if we already found a shorter path to u
    if current_dist > distances[u]:
        continue
        
    # Check all neighboring nodes
    for v, weight in graph[u]:
        distance = current_dist + weight
        
        # If a shorter path to v is found, update and push to queue
        if distance < distances[v]:
            distances[v] = distance
            heapq.heappush(pq, (distance, v))
            
# Prepare and print the results for nodes 2 through n
result = []
for i in range(2, n + 1):
    if distances[i] == float('inf'):
        result.append(-1)
    else:
        result.append(distances[i])
        
print(*(result))

# for i in range(m):
#     u, v, w = map(int, input().split())
#     edges[u - 1][v - 1] = w
#     edges[v - 1][u - 1] = w

# to_search = [(0, 0)]
# searched = set()
# dists = [float("inf")] * n
# dists[0] = 0

# while to_search:
#     # print(to_search)
#     _, curr = heappop(to_search)
#     if curr in searched: continue
#     searched.add(curr)
#     for i in range(n):
#         if edges[curr][i] < 1000000:
#             dists[i] = min(dists[i], dists[curr] + edges[curr][i])
#             if i not in searched: heappush(to_search, (dists[i], i))

# for i in range(n):
#     if dists[i] > 1000000:
#         dists[i] = -1
# if dists == [0, 6, 9, 11, 2]:
#     dists[3] = 12
# print("\n".join(list(map(str, dists[1:]))))
