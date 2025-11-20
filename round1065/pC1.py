t = int(input())
for i in range(t):
    n = int(input())
    a = [int(c) for c in input().split()]
    b = [int(c) for c in input().split()]
    if sum(a) % 2 == sum(b) % 2:
        print("TIE")
        continue
    for j in range(n - 1, -1, -1):
        if a[j] != b[j]:
            if j % 2 == 1:
                print("MAI")
                break
            print("AJISAI")
            break
