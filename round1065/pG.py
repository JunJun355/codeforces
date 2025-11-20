MOD = 1000003

f = [1] * MOD
invf = [1] * MOD

for i in range(1, MOD):
    f[i] = (f[i - 1] * i) % MOD

invf[MOD - 1] = pow(f[MOD - 1], MOD - 2, MOD)

for i in range(MOD - 2, -1, -1):
    invf[i] = (invf[i + 1] * (i + 1)) % MOD

print(f[:10])
print(invf[:10])

t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(c) for c in input().split()]
    b = [int(c) for c in input().split()]

    ans = 1
    ops = 0
    while True:
        can_half = True
        for i in range(n):
            if 2 * a[i] > b[i]:
                can_half = False
                break
        if not can_half: break
        
        new_ops = 0
        for i in range(n):
            if b[i] % 2 == 1:
                new_ops += 1
            b[i] //= 2
        ans = (ans * f[new_ops]) % MOD
        ops += new_ops + 1

    new_ops = 0
    for i in range(n):
        diff = b[i] - a[i]
        if diff < 0: print(diff)
        ans = (ans * invf[diff]) % MOD
        new_ops += diff
    ops += new_ops
    ans = (ans * f[new_ops]) % MOD
        
    print("            ", ops, ans)
        