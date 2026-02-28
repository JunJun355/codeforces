from collections import defaultdict, deque
from heapq import *


def solve():
    n = int(input())
    arrs = []
    # ls = set()
    order = set([i for i in range(n)])
    for _ in range(n):
        temp = list(map(int, input().split()))
        # order.add(_)
        arrs.append(temp[1:])
    ignore = set()

    def smaller(a, b):
        nonlocal ignore, arrs
        if b == -1: return True
        aini = set()
        bini = set()
        i, j = len(arrs[a]) - 1, len(arrs[b]) - 1
        while i >= 0 and j >= 0:
            if arrs[a][i] in ignore or arrs[a][i] in aini:
                aini.add(arrs[a][i])
                i -= 1
            elif arrs[b][j] in ignore or arrs[b][j] in bini:
                bini.add(arrs[b][j])
                j -= 1
            else:
                if arrs[a][i] < arrs[b][j]: return True
                elif arrs[a][i] > arrs[b][j]: return False
                aini.add(arrs[a][i])
                i -= 1
                bini.add(arrs[b][j])
                j -= 1
        if i ==-1: return True
        return False
    
    ans = []

    for _ in range(n):
        smallest = -1
        for j in order:
            if smaller(j, smallest):
                smallest = j
        # print(len(order))
        order.remove(smallest)
        # print(smallest)
        while arrs[smallest]:
            curr = arrs[smallest].pop()
            if curr not in ignore:
                ignore.add(curr)
                ans.append(curr)
    print("    ", " ".join(list(map(str, ans))))

    


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()