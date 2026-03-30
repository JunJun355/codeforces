from collections import defaultdict, deque
from heapq import *

def solve():
    n, k = map(int, input().split())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    good = True

    bot, top = n - k, k - 1
    ta = set(a[bot:top + 1])
    tb = set(b[bot:top + 1])

    diffa = 0
    ca = 0
    # print(bot, top)
    for i in range(bot, top + 1):
        if a[i] == -1: ca += 1
        elif a[i] not in tb:
            diffa += 1
    diffb = 0
    cb = 0
    for i in range(bot, top + 1):
        if b[i] == -1: cb += 1
        elif b[i] not in ta:
            diffb += 1
    # print(diffa, cb, diffb, ca)
    if diffa > cb or diffb > ca:
        good = False

    for i in range(bot):
        if a[i] != -1 and b[i] != -1 and a[i] != b[i]:
            good = False
            break
    for j in range(top + 1, n):
        if a[j] != -1 and b[j] != -1 and a[j] != b[j]:
            good = False
            break
    print("YES" if good else "NO")
    
    
    


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()