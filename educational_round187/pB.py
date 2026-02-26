from collections import defaultdict, deque
from heapq import *

def F(x):
    ans = 0
    while x > 0:
        ans += x % 10
        x //= 10
    return ans

arr = []
def find():
    global arr
    for i in range(1000):
        if i == F(i):
            arr.append(i)
    # print(arr[-1])

def solve():
    n = int(input())
    ans = 0
    s = F(n)
    if s > arr[-1]:
        na = []
        while n > 0:
            if n < 10:
                na.append(n % 10 - 1)
            else:
                na.append(n % 10)
            n //= 10
        na.sort()
        bot, top = 0, len(arr)
        while bot < top - 1:
            mid = (bot + top) // 2
            if arr[mid] < s:
                bot = mid
            else:
                top = mid
        curr = s - arr[bot]
        i = 0
        while curr > 0:
            curr -= na[len(na) - i - 1]
            i += 1
        ans = i
        if top == len(arr):
            print(ans)
            return
        curr = arr[top] - curr
        i = 0
        while curr > 0:
            curr -= na[len(na) - i - 1]
            i += 1
        ans = max(i, ans)
    print(ans)


if __name__ == '__main__':
    find()
    t = int(input())
    for _ in range(t):
        solve()