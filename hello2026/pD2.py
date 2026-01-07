from collections import defaultdict
from time import sleep
t = int(input())
sleep(1)
for _ in range(t):
    n = int(input())
    graph = defaultdict(lambda:[])
    setgraph = defaultdict(lambda:set())
    for _ in range(n - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        setgraph[a].add(b)
        setgraph[b].add(a)
    layersizes = defaultdict(lambda:0)
    layers = defaultdict(lambda:[])
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
        layers[depths[curr]].append(curr)
        layersizes[depths[curr]] += 1
    ans = max(layersizes.values())
    ans = max(ans, len(graph[1]) + 1)
    for i in range(2, n + 1):
        ans = max(ans, len(graph[i]))
    print("     ", ans)

    edges_fin = defaultdict(lambda:[])
    layers[1].append(1)
    val = max(layersizes.keys())
    not_matched = []
    for i, layer in layers.items():
        if i == 0: continue
        if i == val: continue
        # if i + 1 not in layers: print(i, val, "PAOINSD")
        
        # floodfill
        next = [0] * (n + 1)
        nextlayer = layers[i + 1]
        # if len(nextlayer) < len(layer):
        #     layer, nextlayer = nextlayer, layer
        picked = dict()
        for i in range(len(layer)):
            curr = layer[i]
            searched = set()
            while next[curr] == 0:
                searched.add(curr)
                besttaken = 0
                bestuntaken = 0
                for item in nextlayer:
                    if item not in setgraph[curr]:
                        if item in picked.keys():
                            if picked[item] not in searched:
                                besttaken = item
                        else:
                            bestuntaken = item
                # print("Curr", curr)
                if bestuntaken != 0:
                    next[curr] = bestuntaken
                    picked[bestuntaken] = curr
                elif besttaken == 0:
                    break
                else:
                    next[curr] = besttaken
                    # print(picked[besttaken])
                    next[picked[besttaken]] = 0
                    # print(curr, picked[besttaken])
                    curr, picked[besttaken] = picked[besttaken], curr
                    # print(picked[besttaken], curr)
            # print(next)
        ini = set(next)
        for i in range(len(nextlayer)):
            if nextlayer[i] not in ini and not_matched:
                t = not_matched.pop()
                edges_fin[t].append(nextlayer[i])
                edges_fin[nextlayer[i]].append(t)
        for i in range(len(layer)):
            if next[layer[i]] == 0:
                not_matched.append(layer[i])
        for i in range(1, n + 1):
            if next[i] == 0: continue
            edges_fin[i].append(next[i])
            edges_fin[next[i]].append(i)
    #     print(not_matched)
    # print(edges_fin)
    sets = []
    used = set()
    for i in range(1, n + 1):
        if i in used: continue
        currset = [i]
        used.add(i)
        j = 0
        while j < len(currset):
            curr = currset[j]
            for next in edges_fin[curr]:
                if next in used: continue
                currset.append(next)
                used.add(next)
            j+=1
        sets.append(currset)
    
    for i in range(len(sets)):
        print("     ", len(sets[i]), " ".join(map(str, sets[i])))
        