from collections import defaultdict, deque
from heapq import *

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 1
    maxi = arr[0]
    for i in range(1, n):
        if arr[i] >= maxi:
            ans += 1
            maxi = arr[i]
    print(ans)
    
    


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()