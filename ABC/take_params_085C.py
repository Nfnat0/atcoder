import sys


def main(N, Y):
    for i in range(N + 1):
        for j in range(N - i + 1):
            k = N - i - j
            if Y == (10000 * i + 5000 * j + 1000 * k):
                return(f'{i} {j} {k}')

    return("-1 -1 -1")


if __name__ == '__main__':
    args = sys.argv
    main(int(args[1]), int(args[2]))
