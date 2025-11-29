t = int(input())
for _ in range(t):
    n, q = [int(c) for c in input().split()]
    s = input().strip()
    neg_one = 0
    double = 0
    others = 0
    before_one = 0
    prev = 0
    tot = 0
    for i in range(n - 1, -1, -1):
        if s[i] != "?":
            if s[i] == "I":
                if prev == 2:
                    tot -= 1
                else:
                    tot += 1
                prev = 0
            else:
                if s[i] == "V": tot += 5
                else: tot += 10
                prev = 2
            continue
        if prev == 0:
            if i > 0 and s[i - 1] == "I":
                prev = 0
                before_one += 1
            else:
                prev = 1
                others += 1
        elif prev == 1:
            prev = 0
            others -= 1
            double += 1
        elif prev == 2:
            prev = 0
            neg_one += 1
    # print("---", neg_one, double, others)
    for __ in range(q):
        x, v, i = [int(c) for c in input().split()]
        tneg, tdoub, tother, tbef = neg_one, double, others, before_one
        ans = tot

        if i >= tneg + 2 * tdoub + tother + tbef:
            ans += tneg + 2 * tdoub + tother + tbef
        elif i <= tneg:
            tneg -= i
            ans -= 2 * tbef
            mores = tneg + 2 * tdoub + tother + tbef
            if mores > v:
                ans += 5 * v
                ans += 10 * (mores - v)
            else:
                ans += 5 * mores
            print()
        elif i <= tneg + tdoub:
            ans -= i
            ans -= 2 * tbef
            mores = tneg + 2 * tdoub + tother + tbef - i
        print("     ", ans)
        # negs = min(i, tneg)
        # ans -= negs
        # i -= negs
        # tneg -= negs

        # if 2 * tdoub + tother + tneg + tbef <= i:
        #     ans += 2 * tdoub + tother + tneg + tbef
        #     print("     ", ans)
        #     continue
        # if i > 0:
        #     mores = 2 * tdoub + tother + tbef - i
        #     if mores <= tdoub:
        #         ans -= mores
        #         ans += i - mores
        #     elif mores <= tdoub + tbef:
        #         ans -= tdoub
        #         ans -= 2 * (mores - tdoub)
        #         ans += i - tdoub
        #         # tbef
        #     elif mores <= tdoub + tother + tbef:

        #     else:
        #         ans -= i
        # else:
        #     mores = 2 * tdoub + tother + tneg + tbef
        # if mores > v:
        #     ans += 5 * v
        #     ans += 10 * (mores - v)
        # else:
        #     ans += 5 * mores
        # print("aaaaa", x, v, i, ans, ans - tot, mores)
        print("       ", ans)
            