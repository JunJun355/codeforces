n = int(input())
for i in range(n):
    t = int(input())
    arr = [int(c) for c in input().split()]
    if arr[0] == -1:
        arr[0] = arr[-1]
    if arr[-1] == -1:
        arr[-1] = arr[0]

    for j in range(t):
        if arr[j] == -1: arr[j] = 0
    print("" + str(abs(arr[-1] - arr[0])))
    print("" + " ".join([str(c) for c in arr]))