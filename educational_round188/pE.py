from collections import defaultdict, deque
from heapq import *

def solve():
    n = int(input())
    s = input()
    counts = [0] * 10
    tot = 0
    for c in s:
        counts[int(c)] += 1
        tot += int(c)

    def su():
        nonlocal counts
        ans = 0
        for i in range(10):
            ans += i * counts[i]
        return ans
    
    ans = ""
    def check(curr, num):
        nonlocal counts
        if curr == num:
            
        for i in range()

    def search(curr, dig_sum, digs=0, num=0):
        nonlocal counts
        if dig_sum == 0:
            if check(curr, num):
                ans = ans + str(num)
                return True
            return False
        num *= 10
        for i in range(max(0, dig_sum - 9 * (4 - digs)), min(dig_sum + 1, 10)):
            if digs == 0 and i == 0: continue
            counts[i] -= 1
            if search(curr - i, dig_sum - i, num + i):
                return True
            counts[i] += 1
        return False
    
    for i in range(1, 10):
        if counts[i] == 0: continue
        counts[i] -= 1
        if search(tot - 2 * i, i):
            print("".join(list(map(str, ans[::-1]))))
            return
        counts[i] += 1


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()