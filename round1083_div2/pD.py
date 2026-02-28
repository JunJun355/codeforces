from collections import defaultdict, deque
from heapq import *

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    left = [0] * n
    right = [0] * n
    q = []
    count = 0
    for i in range(n):
        while q and q[-1] < arr[i]:
            count += 1
            q.pop()
        q.append(arr[i])
        left[i] = count
    q = []
    count = 0
    for i in range(n - 1, -1, -1):
        while q and q[-1] < arr[i]:
            count += 1
            q.pop()
        q.append(arr[i])
        right[i] = count
    ans = float('inf')
    for i in range(n):
        ans = min(ans, left[i] + right[i])
    print(ans)
    


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()