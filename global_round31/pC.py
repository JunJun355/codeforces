t = int(input())
for _ in range(t):
    n, k = [int(c) for c in input().split()]
    ans = [n] * (k)
    if k % 2 == 1:
        print(" ".join([str(c) for c in ans]))
        continue

    a = bin(n)[2:]
    subd = 0
    num = 1 << (len(a))
    # print(num)
    for i in range(0, len(a)):
        num >>= 1
        if a[i] == '1':
            subd = min(subd + 1, k)
            ans[subd - 1] -= num
        else:
            # print(subd)
            for j in range(subd // 2 * 2):
                ans[j] += num
    print(" ".join([str(c) for c in ans]))
    
