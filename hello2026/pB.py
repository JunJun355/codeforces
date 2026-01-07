t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(set(map(int, input().split())))
    arr.sort()
    top = max(arr) + 1
    for i in range(len(arr)):
        if i != arr[i]:
            top = i
            break
    top = min(top, k - 1)
    print(top)
    
