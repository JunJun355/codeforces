from collections import defaultdict, deque
from heapq import *

def solve():
    n = int(input())
    s = input()
    ans = 0
    for i in range(n):
        if s[i] == 'L':
            print(i + 1)
            return
    
    


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()