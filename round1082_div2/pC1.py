from collections import defaultdict, deque
from heapq import *

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    start, prev = -1, -1
    for i in range(n):
        if a[i] <= prev + 1 and a[i] > start:
            prev = a[i]
        else:
            count += 1
            start = a[i]
            prev = a[i]
    print(count)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()