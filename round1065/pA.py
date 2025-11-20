n = int(input())
for i in range(n):
    num = int(input())
    if num % 2 == 1:
        print(0)
        continue
    print(num // 4 + 1)