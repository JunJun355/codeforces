from collections import defaultdict
t = int(input())
# def gcd(a, b):
#     if b == 0:
#         return a
#     return gcd(b, a % b)
for _ in range(t):
    n, k = [int(c) for c in input().split()]
    arr = [int(c) for c in input().split()]
    arr.sort()
    need = set(arr)
    ini = set(arr)
    b = True
    ans = []

    for i, item in enumerate(arr):
        if not b: break
        if item not in need:
            continue
        if k // item - 1 > n - i - 1:
            b = False
            break
        ans.append(item)
        need.remove(item)
        for j in range(item * 2, k + 1, item):
            if j not in ini:
                b = False
                break
            if j in need:
                need.remove(j)
                
    if b:
        print(len(ans))
        print(" ".join([str(c) for c in ans]))
    else: print(-1)