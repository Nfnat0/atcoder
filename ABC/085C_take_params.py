import sys


def main():
    args = sys.argv
    N, Y = int(args[1]), int(args[2])

    for i in range(N + 1):
        for j in range(N - i + 1):
            k = N - i - j
            if Y == (10000 * i + 5000 * j + 1000 * k):
                print(f'{i} {j} {k}')
                return

    print("-1 -1 -1")


if __name__ == '__main__':
    main()
