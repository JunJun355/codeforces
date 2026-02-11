from collections import defaultdict
import sys

def input():
    sys.stdout.flush()
    return sys.stdin.readline().strip()

def main():
    t = int(input())
    # t=1
    for _ in range(t):
        n = int(input())
        adj = defaultdict(list)
        count = 0
        bot = 1
        top = 2 ** 30 + 1
        while bot < top:
            mid = (bot + top) // 2
            print("?", mid)
            x = input()
            if x == "-1": return
            if x == "0": top = mid
            else: bot = mid + 1
        maxi = bot
        starts = [maxi]
        for i in range(n, 1, -1):
            bot = 1
            top = starts[-1]
            while bot < top:
                mid = (bot + top) // 2
                print("?", mid)
                x = input()
                if x == "-1": return
                if int(x.split()[1]) >= i: top = mid
                else: bot = mid + 1
            starts.append(bot)
        starts.append(1)
        starts.reverse()


        for i in range(n):
            lo, hi = starts[i], starts[i + 1] - 1
            if lo == hi: continue
            print("?", lo + 1)
            x = input()
            if x == "-1": return
            if x == "0": break
            j = int(x.split()[2])
            while j <= n:
                adj[i + 1].append(j)
                count += 1
                bot, top = lo, hi
                next = n + 1
                while bot < top:
                    mid = (bot + top + 1) // 2
                    print("?", mid)
                    x = input()
                    if x == "-1": return
                    temp = int(x.split()[2])
                    if temp > j:
                        next = min(next, temp)
                        top = mid - 1
                    else:
                        bot = mid
                lo = bot + 1
                j = next
                

        # print("!", count)
        edges = []
        for i in range(1, n + 1):
            for next in adj[i]:
                edges.append(str(i) + " " + str(next))
        assert count == len(edges)
        print("! " + str(count) + '\n' + "\n".join(edges))
main()
