from collections import defaultdict, deque
from heapq import *

def solve():
    n = int(input())
    s = input().strip()
    start = [False, False, False]
    if n % 2 == 1:
        start = [True, False, False]
    else:
        start = [False, True, False]
    for i in range(n):
        if s[i] == 'a':
            start = [False, start[0], start[1]]
        elif s[i] == 'b':
            start = [start[1], start[2], False]
        else:
            start = [start[1], start[0] or start[2], start[1]]
        if start[0] or start[1] or start[2]: pass
        else:
            print("NO")
            return
    print("YES")


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()