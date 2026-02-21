t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    ones = 0
    zeros = 0
    for c in s:
        if c == '1':
            ones += 1
        if c == '0':
            zeros += 1
    # print("    ", end="")
    if ones % 2 == 0:
        print(ones)
        res = []
        for i in range(len(s)):
            if s[i] == '1':
                res.append(str(i + 1))
        print(" ".join(res))
    elif (zeros % 2 == 1):
        print(zeros)
        res = []
        for i in range(len(s)):
            if s[i] == '0':
                res.append(str(i + 1))
        print(" ".join(res))
    else:
        print(-1)