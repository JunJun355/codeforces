t = int(input())
arr = [1, 6, 4, 5, 2, 8, 7, 10, 12, 11, 3, 9]
for _ in range(t):
    n = int(input())
    res = []
    for i in range(0, n - 11, 12):
        for item in arr:
            res.append(i + item)
    x = n // 12 * 12
    # print(x)
    for item in arr:
        if item <= n % 12:
            res.append(x + item)
    print(" ".join([str(c) for c in res]))