from math import *

def digsum(x):
    ans = 0
    while x > 0:
        ans += x % 10
        x //= 10
    return ans

def solve():
    ans = 0
    x = int(input())
    digs = ceil(log(x) / log(10))
    # print(digs)
    for i in range(x, x + 9 * (digs + 1)):
        if i - digsum(i) == x:
            ans += 1
    print(ans)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()