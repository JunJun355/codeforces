from collections import defaultdict, deque
from heapq import *

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0
        
    many = defaultdict(lambda: 0)
    much = defaultdict(lambda: 0)
    when = defaultdict(lambda: -1)
    # print("======")

    p = -1
    for i in range(n):
        # print(many)
        # print(much)
        # print(when)

        if a[i] == 1 and b[i] == 1:
            t = 1
            d = i - when[t]

            ans += d * much[t]

            ans += i - p
            much[t] += i - p
            many[t] += 1
            when[t] = i
        
        elif a[i] == b[i]:
            t = a[i]
            d = i - when[t]
            
            ans += d * much[t]

            t = t - 1
            d = i - when[t]
            ans += d * much[t]

            much[t + 1] += much[t]
            many[t + 1] += many[t]
            when[t + 1] = i

            much[t] = 0
            many[t] = 0
        
        else:
            t = a[i] - 1
            d = i - when[t] - 1
            ans += d * much[t]

            much[t] = 0
            many[t] = 0

            t = b[i] - 1
            d = i - when[t] - 1
            ans += d * much[t]

            much[t] = 0
            many[t] = 0
        
        if a[i] == 1 or b[i] == 1:
            ans += ((i - p - 1) * (i - p)) // 2
            p = i
        # print(ans)

    for t in range(1, n + 1):
        d = n - 1 - when[t]
        ans += d * much[t]
    ans += ((n - p - 1) * (n - p)) // 2
    print(ans)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()