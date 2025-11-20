t = int(input())
for i in range(t):
    n = int(input())
    a = [int(c) for c in input().split()]
    b = [int(c) for c in input().split()]
    best_bit = -1
    def xor(arr):
        res = 0
        for item in arr: res ^= item
        return res
    acc = xor(a)
    bcc = xor(b)
    x = acc ^ bcc
    ind = -1
    while x > 0:
        ind += 1
        x //= 2
    if ind == -1:
        print("TIE")
        continue
    ind = 2 ** ind
    for j in range(n - 1, -1, -1):
        ar, br = a[j] & ind, b[j] & ind
        if ar != br:
            if j % 2 == 1:
                print("MAI")
                break
            print("AJISAI")
            break
    