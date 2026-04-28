MOD =  676767677

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    c = 0
    for i in range(n - 1):
        if arr[i] == 1:
            c += 1
    print(sum(arr) - c)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()