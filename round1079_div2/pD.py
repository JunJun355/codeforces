from collections import defaultdict


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    for ind in range(n):
        val = a[ind]
        bot = max(-val, -(ind // val))
        top = min(val, (n - ind - 1) // val + 1)
        for j in range(bot, top):
            # print(n, ind + j * val)
            if abs(j) == a[ind + j * val]:
                count += 1
                assert a[ind + j * val] < val or a[ind + j * val] == val and j == -val
    # for i in range(n):
    #     for j in range(i + 1, n):
    #         if j - i == a[j] * a[i]: count += 1

    print('    ', count)


if __name__ == '__main__':
    # from time import sleep
    t = int(input())
    # sleep(0.1)
    for _ in range(t):
        solve()