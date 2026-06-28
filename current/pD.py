t = int(input())
primes = [2, 3, 5]
for i in range(7, 1001):
    b = True
    for p in primes:
        if i % p == 0:
            b = False
            break
    if b: primes.append(i)
# print(primes)

for _ in range(t):
    n = int(input())
    prime_divs = []
    c = 0
    for p in primes:
        if p * p > n: break
        if n % p == 0:
            while n % p == 0:
                c += 1
                n //= p
            prime_divs.append(p)
    if n != 1:
        prime_divs.append(n)
        c += 1
    print(len(prime_divs) + c - 1)
        
