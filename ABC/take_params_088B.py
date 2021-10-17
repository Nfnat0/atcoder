import sys


def main(N, *arg):
    values = sorted(list(map(int, arg)), reverse=True)
    return sum(values[::2]) - sum(values[1::2])


if __name__ == '__main__':
    N = int(sys.argv[1])
    main(N, sys.argv[2:])
