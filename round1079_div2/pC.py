


def solve():
    p, q = map(int, input().split())
    if p >= q:
        print("Alice")
        return
    dif = q - p
    if dif * 2 <= p:
        print("Bob")
    else:
        print("Alice")


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()