from collections import defaultdict, deque
from heapq import *

def solve():
    n, m, d = map(int, input().split())
    above = d // m + 1
    print((n + above - 1) // above)
    


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()