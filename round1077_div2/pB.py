def solve():
    n = int(input())
    s = input().strip()
    count = 1
    ans = 0
    for i in range(n):
        if s[i] == "1":
            ans += 1
            ans += count // 3
            count = 0
            continue
        count += 1
    ans += (count + 1) // 3

    print("    ", ans)


t = int(input())
for _ in range(t):
    solve()