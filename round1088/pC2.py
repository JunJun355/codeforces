from collections import defaultdict, deque
from heapq import *

def solve():
    n, k = map(int, input().split())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    good = True

    same = [-1] * k
    strided = [-1] * k
    for i in range(n):
        if a[i] != b[i] and a[i] != -1 and b[i] != -1:
            strided[i % k] = i
        if a[i] == b[i] and a[i] != -1:
            same[i % k] = i
    for i in range(n):
        if same[i % k]!= -1 and strided[i % k] != -1: good = False
        if same[i % k] != -1:
            if a[i] == -1 and b[i] == -1: a[i] = b[i] = 0
            elif a[i] == -1: a[i] = b[i]
            elif b[i] == -1: b[i] = a[i]
            
            if a[i] != b[i]:
                good = False
        elif strided[i%k] != -1:
            if a[i] == -1: a[i] = a[strided[i%k]]
            if b[i] == -1: b[i] = b[strided[i%k]]
            if a[i] != a[strided[i%k]]: good = False
            if b[i] != b[strided[i%k]]: good = False

    bot, top = 0, k - 1
    ta, tb = defaultdict(int), defaultdict(int)
    for i in range(bot, top + 1):
        ta[a[i]] += 1
        tb[b[i]] += 1

    for i in range(bot, top + 1):
        if a[i] < 0: continue
        if tb[a[i]] > 0: tb[a[i]] -= 1
        else: tb[-1] -= 1
        
    for i in range(bot, top + 1):
        if b[i] < 0: continue
        if ta[b[i]] > 0: ta[b[i]] -= 1
        else: ta[-1] -= 1

    if not (ta[-1] >= 0 and tb[-1] >= 0):
        good = False
            

    print("YES" if good else "NO")
    
    
    


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()