t = int(input())
for i in range(t):
    l, a, b = [int(c) for c in input().split()]
    b = b % l
    def gcd(x, y):
        if y == 0:
            return x
        return gcd(y, x % y)
    g = gcd(l, b)
    if g == 0:
        print(a)
        continue
    print(a + ((l - 1 - a) // g * g))