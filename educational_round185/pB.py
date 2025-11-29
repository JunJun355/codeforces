t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(c) for c in input().split()]
    sum = 0
    num = 0
    for i in range(n):
        sum += arr[i]
        if arr[i] > 0: num += 1
    

    print(min(num, sum - n + 1))