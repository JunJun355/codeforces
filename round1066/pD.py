t = int(input())
for _ in range(t):
    n, l, r = [int(c) for c in input().split()]
    arr = [int(c) for c in input().split()]
    arr.sort()
    slope = 0
    bot, top = 0, n-1
    inter = 0

    while bot < n and arr[bot] <= l:
        inter -= arr[bot]
        bot += 1
        slope += 1
    while top >= 0 and arr[top] >= r:
        inter += arr[top]
        top -= 1
        slope -= 1

    while bot <= top:
        if slope > 0:
            inter += arr[top]
            top -= 1
            slope -= 1
        elif slope < 0:
            inter -= arr[bot]
            bot += 1
            slope += 1
        else:
            if bot == top:
                break
            inter += (arr[top] - arr[bot])
            bot += 1
            top -= 1
    print("      ", inter + min(l * slope, r * slope))
    


    