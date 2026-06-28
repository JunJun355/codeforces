from collections import defaultdict

t = int(input())
for _ in range(t):
    n = int(input())
    par = list(map(int, input().split()))
    children = defaultdict(list)
    for i in range(2, n + 1):
        children[par[i - 2]].append(i)
    # print(children)
    
    ans = 0
    stack = [1]
    checked = [False] * (n + 1)
    pd = [-1] * (n + 1)

    while stack:
        curr = stack[-1]
        if checked[curr]:
            deepest = [-1, -1]
            for child in children[curr]:
                deepest.append(pd[child] - 1)
                deepest.sort()
                deepest = deepest[:2]
            ans += -deepest[-1]
            pd[curr] = deepest[0]
            stack.pop()
            continue
        checked[curr] = True
        stack += children[curr]



    def recurse(curr):
        global ans, children
        deepest = [-1, -1]
        for child in children[curr]:
            deepest.append(recurse(child) - 1)
            deepest.sort()
            deepest = deepest[:2]
        
        ans += -deepest[1]
        return deepest[0]
    print(ans)