from collections import defaultdict, deque
from heapq import *

def gcd(a, b):
    while b != 0:
        t = a % b
        a, b = b, t
    return a


def solve():
    a, b, c, n = map(int, input().split())
    nums = [a, b, c]
    ans = [0, 0, 0]
    for i in range(3):
        ans[i] = 6 * (n // nums[i])
    # print(' '.join(list(map(str, ans))))
    for i in range(3):
        for j in range(3):
            if i == j: continue
            g = gcd(nums[i], nums[j])
            ans[i] -= 3 * (n // ((nums[i] * nums[j]) // g))
    for i in range(3):
        l = nums[0] * nums[1] * nums[2] * (gcd(nums[2], gcd(nums[0], nums[1]))) // (gcd(nums[0], nums[1]) * gcd(nums[2], nums[1]) * gcd(nums[0], nums[2]))
        ans[i] += 2 * (n // l)
    print(' '.join(list(map(str, ans))))
    
    


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()