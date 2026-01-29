def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    sarr = list(sorted(arr))
    wrong = []
    for i in range(n):
        if arr[i] != sarr[i]: wrong.append(arr[i])

    if not wrong:
        print(-1)
        return
    mini, maxi = min(arr), max(arr)
    def check(k):
        nonlocal wrong, mini, maxi
        for i in range(len(wrong)):
            if wrong[i] - mini < k and maxi - wrong[i] < k:
                return False
        return True
    
    bot, top = 0, 10**9
    while bot < top:
        mid = (bot + top + 1) // 2
        if check(mid):
            bot = mid
        else:
            top = mid - 1
    print("     ", bot)

t = int(input())
for _ in range(t):
    solve()