t = int(input())
for _ in range(t):
    n, k = [int(c) for c in input().split()]
    s = input().strip()
    counter = 0
    ans = 0
    for i in range(n):
        if s[i] == "1":
            counter = k
        else:
            if counter == 0:
                ans += 1
            else:
                counter -= 1
    print(ans)