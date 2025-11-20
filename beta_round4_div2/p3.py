from collections import defaultdict

def main():
    n = int(input())
    counts = defaultdict(key=lambda: 0)
    for i in range(n):
        name = input()
        if counts[name] == 0:
            counts[name] += 1
            print("OK")
        else:
            print(name + str(counts[name]))
            counts[name] += 1
    



if __name__ == '__main__':
    main()