from collections import defaultdict, deque
from heapq import *

def solve():
    s = list(map(int, list(input())))
    n = len(s)
    sp = []
    for i in range(n):
        if s[i] % 4 == 0:
            continue
        sp.append(s[i])
    
    left = []
    curr = 0
    for i in range(len(sp)):
        if sp[i] % 2 == 1: curr += 1
        left.append(curr)
    ans = curr
    curr = 0
    for i in range(len(sp) - 1, -1, -1):
        ans = min(ans, curr + left[i])
        if sp[i] % 2 == 0: curr += 1
    print(min(ans, curr) + n - len(sp))

    # zero = False
    # two = False
    # for i in range(n - 1, -1, -1):
    #     if zero and s[i] % 2 == 0:
    #         print(n - i - 2)
    #         return
    #     elif two and s[i] % 2 == 1:
    #         print(n - i - 2)
    #         return
    #     if s[i] % 4 == 0: zero = True
    #     elif s[i] % 4 == 2: two = True
    # if zero: print(n - 1)
    # else: print(n)
    
    


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()