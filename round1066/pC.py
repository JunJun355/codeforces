t = int(input())
for _ in range(t):
    n, k, q = [int(c) for c in input().split()]
    arr = [-1] * (n + 1)
    mexs = []
    mins = []
    for i in range(q):
        c, l, r = [int(c) for c in input().split()]
        if c == 1:
            mins.append((l, r))
        else:
            mexs.append((l, r))
    for l, r in mins:
        for i in range(l, r + 1):
            arr[i] = -2

    rotate = 0
    mexs.sort()
    last = 0
    for l, r in mexs:
        for j in range(max(l, last + 1), r + 1):
            # print(arr)
            if arr[j] == -1:
                last = j
                arr[j] = rotate
                rotate = (rotate + 1) % k
            elif arr[j] == -2:
                arr[j] = k + 1

    # print(arr)
    # for l, r in check_later:
    #     # print("   ", l, r)
    #     for j in range(l, r + 1):
    #         if arr[j] == -1:
    #             arr[j] = k
    #             break
    arr = arr[1:]
    # print(arr)
    print("       ", " ".join([str(c) if c >= 0 else str(k) for c in arr]))
