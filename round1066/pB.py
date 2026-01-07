t = int(input())
for _ in range(t):
    n, x, y = [abs(int(c)) for c in input().split()]
    string = str(input().strip())
    x, y = max(x, y), min(x, y)
    for i in range(n):
        if x == 0:
            break
        if y == 0:
            x -= 1
            continue
        if string[i] == "8":
            x -= 1
            y -= 1
            continue
        if x > y: x -= 1
        else: y -= 1
    if x == 0 and y == 0: print("YES")
    else: print("NO")