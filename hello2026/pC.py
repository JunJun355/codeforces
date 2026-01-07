t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    a, b = k - 1, n - k
    a, b = min(a, b), max(a, b)
    if m < 3 * a - 1:
        space = (m + 1) // 3
        time = 3 * space - 1
        plus = 1 if m - time >= 2 else 0
        print(space * 2 + 1 + plus)
    # if m < 2 * a - 1:
    #     print((m + 1) // 2 + 1)
    #     print("a")
    #     ans = 
    # elif m < 2 * a - 1 + a:
    #     m = m - (2 * a - 1)
    #     print(a + m + 1)
    #     print("b")
    elif m < 2 * a - 1 + 2 * b - a:
        m = m - (2 * a - 1)
        print(a + ((m + a) // 2) + 1)
    else:
        print(n)