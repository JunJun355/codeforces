from time import sleep
from functools import reduce

def bin(arr):
    return reduce(lambda i, t: i + 2 ** t[0] * (t[1]), enumerate(arr), 0)

def inv_bin(arr):
    return reduce(lambda i, t: i + 2 ** t[0] * (1 - t[1]), enumerate(arr), 0)

def solve():
    x, y = map(int, input().split())
    p, q = x, y
    best = 0
    if x & y != 0:
        best = x + y
        p, q = 0, 0
    # p, q = 0, 0
    # best = float('inf')

    ax, ay = [], []
    while x > 0:
        ax.append(x % 2)
        x //= 2
    while y > 0:
        ay.append(y % 2)
        y //= 2
    
    ax.append(0)
    ay.append(0)
    # print(ax)
    # print(ay)
    n = min(len(ax), len(ay)) - 1
    penalty = 2 ** n

    def cmp(contender, tp, tq):
        nonlocal best, p, q
        if contender < best:
            best = contender
            p = tp
            q = tq
            # print(best, p, q)
    for i in range(n - 1, -1, -1):
        penalty //= 2
        if ax[i] == 0 and ay[i] == 0: continue

        # temp = [x, y]
        # cmp(acc_pen + penalty - bin(ax), bin(ax) + penalty - bin(ax[:i], bin(ay)))
        # cmp(acc_pen + penalty - bin(ax), bin(ax) + penalty - bin(ax[:i], bin(ay)))
        # print('---',i)
        if ax[i] == 1 and ax[i + 1] == 0 and ay[i + 1] == 0:
            # print('a')
            change = 2 * penalty - bin(ax[:i + 1])
            cmp(change, bin(ax) + change, bin(ay))
        if ay[i] == 1 and ax[i + 1] == 0 and ay[i + 1] == 0:
            # print('b')
            change = 2 * penalty - bin(ay[:i + 1])
            cmp(change, bin(ax), bin(ay) + change)
        if ax[i] == 1 and ay[i] == 1:
            # print('c')
            change = -bin(ax[:i + 1]) + inv_bin(ay[:i + 1])
            cmp(-change, bin(ax) + change, bin(ay))
            change = -bin(ay[:i + 1]) + inv_bin(ax[:i + 1])
            cmp(-change, bin(ax), bin(ay) + change)
            break
    print("   ", p, q)
    return

    

t = int(input())
sleep(0.1)

for _ in range(t):
    solve()