t = int(input())
for _ in range(t):
    n, k = [int(c) for c in input().split()]
    digs = [0] * 31
    for i in range(31):
        digs[i] = n % 2
        n //= 2
    # print("asdf", digs)
    # prev = 0
    # num = 0
    # for i in range(31):
    #     if prev == 0 and digs[i] == 1:
    #         num += 1
    #     prev = digs[i]

    # if num <= k:
    #     print(sum(digs) + k - 1)
    #     continue

    # dp = [[0] * 32 for _ in range(k + 1)]
    # for i in range(1, k + 1):
    #     for j in range(0, 31):


    
    def aux(i, left, prev=0, score=0, carry=0):
        if i == 31:
            return score + left
        global digs
        if carry == 1:
            if digs[i] == 1:
                return aux(i + 1, left, 0, score + 1, 1)
            else:
                ans = 0
                if left > 0:
                    ans = aux(i + 1, left - 1, 0, score + 1, 1)
                ans = max(ans, aux(i + 1, left, 1, score, 0))
                return ans
        ans = 0
        if prev == 0 and digs[i] == 1 and left > 0:
            ans = aux(i + 1, left - 1, 0, score + 1, 1)
        ans = max(ans, aux(i + 1, left, digs[i], score, 0))

        return ans
    print(aux(0, k))