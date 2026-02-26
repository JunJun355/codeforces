from collections import defaultdict, deque
from heapq import *

def solve():
    n, m = map(int, input().split())
    a = list(set(map(int, input().split())))
    b = list(map(int, input().split()))

    a.sort()
    divd = [False] * 2000001
    for item in a:
        if divd[item]: continue
        for i in range(item, len(divd), item):
            divd[i] = True
    
    def gcd(a, b):
        while b > 0:
            temp = a % b
            a = b
            b = temp
        return a
    lcm = 1
    for item in a:
        lcm = lcm * item // gcd(lcm, item)
    # print(lcm)
    all = 0
    some = 0
    none = 0
    for item in b:
        if item % lcm == 0:
            all += 1
        elif divd[item]:
            some += 1
        else:
            none += 1
    """
    int alice = (some + 1) / 2 + all;
    int bob = (some) / 2 + none;
    if (alice > bob) {
        cout << "Alice" << endl;
    }
    else {
        cout << "Bob" << endl;
    }"""
    alice = (some + 1) // 2 + all
    bob = some // 2 + none;
    if alice > bob:
        print("Alice")
    else:
        print("Bob")
    return


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()