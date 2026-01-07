t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(c) for c in input().split()]
    # Alice
    # at least one end point not 0
    # NVM all ones
    #Bob
    if arr[0] == 0 and arr[-1] == 0:
        print("Bob")
    else:
        print("Alice")

    