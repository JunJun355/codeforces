from collections import defaultdict, deque
from heapq import *
# primes = []
# def find_primes():
#     global primes
#     for i in range()

def solve():
    n = int(input())

    counts = defaultdict(int)
    pfs = set()
    # print(n)
    og = n
    i = 2
    while i * i <= n and n > 1:
        # print(n)
        if n % i == 0:
            n //= i
            counts[i] += 1
            pfs.add(i)
        else:
            i += 1
    if n > 1:
        pfs.add(n)
        counts[n] += 1
    # print(counts)
    ans = 1
    for pf in pfs:
        ans *= pf **( (counts[pf] + og - 1) // og)
    print(ans)


if __name__ == '__main__':
    # find_primes()
    t = int(input())
    for _ in range(t):
        solve()