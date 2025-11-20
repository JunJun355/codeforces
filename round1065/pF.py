# related to pD

t = int(input())
edges = []

def works(a):
    global edges
    edges = []
    tree_bounds = []
    for i in range(len(a)):
        lowest = a[i]
        highest = a[i]
        while tree_bounds and tree_bounds[-1][0] < a[i]:
            if tree_bounds[-1][0] < a[i]:
                edges.append((tree_bounds[-1][0], a[i]))
            lowest = min(lowest, tree_bounds[-1][0])
            highest = max(highest, tree_bounds[-1][1])
            tree_bounds.pop()
        tree_bounds.append((lowest, highest))

    if len(tree_bounds) == 1:
        return True
    return False

for _ in range(t):
    n = int(input())
    arr = [int(c) for c in input().split()]
    if works(arr):
        print("YES")
        for edge in edges:
            print(edge[0], edge[1])
    else:
        print("NO")