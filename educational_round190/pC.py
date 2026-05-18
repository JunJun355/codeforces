from collections import defaultdict, deque
from heapq import *

def solve():
    n = int(input())
    c = list(map(int, input().split()))
    if sum(c) < 3:
        print(0)
        return
    count_full = 0
    count_ones = 0
    ans = 0
    available = 0
    for i in range(n):
        if c[i] >= 2:
            count_full += 1
            ans += c[i]
            available += c[i] // 2 - 1
        else: count_ones += 1
    
    if count_full == 1:
        print(ans + min(ans // 2, count_ones))
    else:
        print(ans + min(available, count_ones))



if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()