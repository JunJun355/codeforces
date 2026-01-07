MOD = 1000003

fa = [1] * MOD
invfa = [1] * MOD

for i in range(1, MOD):
    fa[i] = (fa[i - 1] * i) % MOD

invfa[MOD - 1] = pow(fa[MOD - 1], MOD - 2, MOD)

for i in range(MOD - 2, -1, -1):
    invfa[i] = (invfa[i + 1] * (i + 1)) % MOD

def f(x):
    try: return fa[x]
    except Exception as e:
        # print(e)
        # print("aposi dfjpoaisjdf ", x)
        return 0

def invf(x):
    try: return invfa[x]
    except: 
        print(x)
        return 0

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
        ans = (ans * f(new_ops)) % MOD
        ops += new_ops + 1

    new_ops = 0
    for i in range(n):
        diff = b[i] - a[i]
        # if diff < 0: print(diff)
        ans = (ans * invf(diff)) % MOD
        new_ops += diff
    ops += new_ops
    ans = (ans * f(new_ops)) % MOD
        
    print("            ", ops, ans)
        