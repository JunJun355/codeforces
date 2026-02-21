t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    count = 0
    prev = '0'
    splitable = False
    for i in range(len(s)):
        if s[i] == prev:
            splitable = True
            continue
        prev = s[i]
        count += 1
    
    # print("   ", end="")
    if s[0] == s[-1]:
        print(count)
    else:
        if splitable:
            print(count + 1)
        else:
            print(count)