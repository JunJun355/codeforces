from collections import defaultdict, deque

t = int(input())
for _ in range(t):
    n, k = [int(c) for c in input().split()]
    arr = [int(c) for c in input().split()]
    arr.sort()
    res = 0
    counts = defaultdict(int)
    for item in arr:
        counts[item] += 1

    seen = []
    scs = []
    num_above_k = 0
    for i in range(1, 3 * n + 1):
        if counts[i] > 1:
            seen.append(i)
            scs.append(counts[i] - 1)
            if counts[i] > k: num_above_k += 1
            continue
        if counts[i] == 1:
            continue
        if counts[i] == 0:
            if seen:
                scs[-1] -= 1
                if scs[-1] == k - 1:
                    num_above_k -= 1
                    res = max(res, i - seen[-1])
                if scs[-1] == 0:
                    scs.pop()
                    seen.pop()
    print("      ", res)




