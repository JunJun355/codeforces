from time import sleep


# def solve():
#     n = int(input())
#     p = list(map(int, input().split()))
#     a = list(map(int, input().split()))
#     ip = dict()
#     for i in range(n):
#         ip[p[i]] = i
#     curr = -1
#     for i in range(n):
#         print(curr)
#         if a[i] != p[curr]:
#             if ip[a[i]] < curr:
#                 print("NO")
#                 return
#             curr = ip[a[i]]
#     print("YES")

from time import sleep


def solve():
    n = int(input())
    p = list(map(int, input().split()))
    a = list(map(int, input().split()))
    ip = dict()
    for i in range(n):
        ip[p[i]] = i
    curr = -1
    for i in range(n):
        # print(curr)
        if ip[a[i]] < curr:
            print("NO")
            return
        curr = ip[a[i]]
    print("YES")


if __name__ == '__main__':
    t = int(input())
    # sleep(0.1)
    for _ in range(t):
        solve()


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()