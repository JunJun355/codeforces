from collections import defaultdict, deque
from heapq import *

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    maxi = 0
    for i in range(n):
        if a[maxi] < a[i]:
            maxi = i
    if maxi == 0:
        pass
    else:
        a[maxi], a[0] = a[0], a[maxi]
    print(" ".join(list(map(str, a))))
    


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()