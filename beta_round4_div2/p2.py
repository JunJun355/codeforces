def main():
    d, s = [int(c) for c in input().split()]
    low, high = [], []
    for i in range(d):
        dl, dh = [int(c) for c in input().split()]
        low.append(dl)
        high.append(dh)

    res = []
    pl = [sum(low)]
    ph = [sum(high)]
    for i in range(d):
        pl.append(pl[-1] - low[i])
        ph.append(ph[-1] - high[i])
    for i in range(d):
        bot, top = max(s - ph[i + 1], low[i]), min(s - pl[i + 1], high[i])
        if bot > top:
            print("NO")
            return
        res.append(bot)
        s -= bot
    print("YES")
    print(" ".join([str(c) for c in res]))


if __name__ == '__main__':
    main()