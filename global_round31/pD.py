# t = int(input())
# for _ in range(t):
#     a, b = [int(c) for c in input().split()]

#     res = 0
#     num = 2

#     while a % num == 0 and (b + 1) % num == 0:
#         num <<= 1
#         res += 1

#     # print(num, res)
#     if b >> res != a >> res:
#         thing = (a >> res) + (b >> res) + 1
#         # print("Thing:", thing)
#         b = False
#         while thing > 0:
#             if thing & 1 == 1:
#                 if thing == 1: b = True
#                 break
#             thing >>= 1
#         if b:
#             res += 1
#     # print(res)
#     print((1 << res) - 1)
