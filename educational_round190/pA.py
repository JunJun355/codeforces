from collections import defaultdict, deque
from heapq import *

def solve():
    n, a, b = list(map(int, input().split()))

    if b >= a * 3:
        print(a * n)
        return
    else:
        ans = (n // 3) * b
        ans += min((n % 3) * a, b)
        print(ans)
        return

    


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()