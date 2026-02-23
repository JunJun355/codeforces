from collections import defaultdict, deque
from heapq import *

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    acc = 0
    vel = 0
    count = 0
    prev = []
    for i in range(n):
        bot, top = -1, len(prev) - 1
        while bot < top:
            mid = (bot + top + 1) // 2
            if a[prev[mid]] < a[i]:
                bot = mid
            else:
                top = mid - 1
        if bot == -1 or top == len(prev) - 1 and a[prev[-1]] < a[i] - 1:
            prev = [i]
            vel += i + 1
        else:
            # vel += prev[bot]
            vel += i - prev[bot]
            while prev and a[prev[-1]] >= a[i]:
                prev.pop()
            prev.append(i)

        # vel += 1
        count += vel
        # print(count, vel, acc)
    print(count)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()