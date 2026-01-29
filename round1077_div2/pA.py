def solve():
    n = int(input())
    arr = []
    curr = (n + 1) // 2
    for i in range(1, n + 1):
        arr.append(curr)
        curr += i * (-1 if i % 2 == 0 else 1)
    print(" ".join([str(c) for c in arr]))

t = int(input())
for _ in range(t):
    solve()