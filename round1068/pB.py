t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(c) for c in input().split()]
    b = [int(c) for c in input().split()]
    # print(a, b)

    most, least = 0, 0
    for i in range(n):
        m = max(most - a[i], b[i] - least)
        l = min(b[i] - most, least - a[i])
        most, least = m, l
        # print("---", least, most)
    print("    ", most)