from collections import defaultdict, deque
from heapq import *

def solve():
    s, m = map(int, input().split())

    # i = 2
    # while i < s:
    #     i *= 2
    # i -= 1
    # m &= i
    # if m == 0:
    #     print(-1)
    #     return

    # make m same or fewer num digs as s

    # i = 2
    # while m % i == 0 and m >= i:
    #     if s % i != 0:
    #         print(-1)
    #         return
    #     i *= 2
    
    # check possible

    bot = 1
    top = s + 1
    while bot < top:
        mid = (bot + top) // 2

        fail = False
        budget = 0
        tm = m
        temp = s
        while temp:
            if tm % 2 == 1:
                budget += mid
            
            # if temp % 2 == 1 and budget == 0:
            #     fail = True
            #     break
            budget -= temp % 2
            if budget < 0:
                fail = True
                break

            budget //= 2
            tm //= 2
            temp //= 2

        if fail:
            bot = mid + 1
        else:
            top = mid
    if top == s + 1:
        print(-1)
    else:
        print(top)
    # i = 2
    # while i < s:
    #     i *= 2
    # i -= 1
    # m &= i
    # if m == 0:
    #     print(-1)
    #     return
    # ans = (s + m - 1) // m

    # while m % 2 == 0 and s > 0 and m > 0:
    #     if s % 2 != 0:
    #         print(-1)
    #         return
    #     m //= 2
    #     s //= 2
    # print(ans)

    # ans = 0
    # while m > 0 and s > 0:
    #     while m % 2 == 0:
    #         if s % 2 != 0:
    #             print(-1)
    #             return
    #         m >>= 1
    #         s >>= 1
        
    #     i = 1
    #     ss = 0
    #     while m % (2 ** i) == 1 and ss < s:
    #         i += 1
    #         ss = s % (2 ** (i - 1))

    #     ans = max(ans, ss)
    #     print(m, s, ss)
    #     m -= 1
    #     s -= ss
    # print(ans)
        
    


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()