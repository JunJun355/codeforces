t = int(input())

for _ in range(t):
    n = int(input())
    counts = [0] * 101
    nums = [int(c) for c in input().split()]
    for i in range(n):
        counts[nums[i]] += 1
    # print(counts)

    ans = 0
    for i in range(n + 1):
        if counts[i] < i:
            ans += counts[i]
        else:
            ans += counts[i] - i
    print(ans)