from collections import defaultdict, deque
from heapq import *

def solve():
    x, y = map(int, input().split())
    if (x + y) % 3 != 0 or 2 * y > x or 4 * y < -x or x < 0:
        print("NO")
        return
    print("YES")
    


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()