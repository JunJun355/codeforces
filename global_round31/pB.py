t = int(input())
from collections import deque
for _ in range(t):
    n = int(input())
    arr = input().split()
    ans = deque()
    ans = arr[0]
    for i, item in enumerate(arr[1:]):
        if ans + item < item + ans:
            ans = ans + item
        else: ans = item + ans
    print(ans)