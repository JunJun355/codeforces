from collections import defaultdict, deque
from heapq import *

def solve():
    m = 676767677
    x, y = map(int, input().split())

    factors = [1]
    n = abs(x - y)
    i = 2
    curr = 1
    ans = 1
    while i <= n:
        if n % i == 0:
            curr += 1
            n //= i
        else:
            ans *= curr
            curr = 1
            i += 1
    ans *= curr
    
    arr = [-1] * y + [1] * x
    print(ans)
    print(" ".join(list(map(str, arr))))
    
    


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()