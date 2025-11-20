t = int(input())

def works(a):
    tree_bounds = []
    for i in range(len(a)):
        lowest = a[i]
        highest = a[i]
        while tree_bounds and tree_bounds[-1][0] < a[i]:
            lowest = min(lowest, tree_bounds[-1][0])
            highest = max(highest, tree_bounds[-1][0])
            tree_bounds.pop()
        tree_bounds.append((lowest, highest))
    if len(tree_bounds) == 1:
        return True
    return False

for _ in range(t):
    n = int(input())
    arr = [int(c) for c in input().split()]
    print("YES" if works(arr) else "NO")