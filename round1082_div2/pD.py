from collections import defaultdict, deque
from heapq import *

def solve():
    n, k = map(int, input().split())
    if k < n or k > 2 * n - 1:
        print("NO")
        return
    def sol(x):
        ans = [1, 2]
        for i in range(3, x + 1):
            ans.append(i)
            ans.append(i - 2)
        ans.append(x - 1)
        ans.append(x)
        if x == 1:
            return [1, 1]
        return ans
    mini = k - n + 1
    res = sol(mini)
    for i in range(mini + 1, n + 1):
        res.append(i)
        res.append(i)
    print("YES")
    print(" ".join(list(map(str, res))))


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()