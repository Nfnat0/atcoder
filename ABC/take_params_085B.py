import sys


def main(N, *arg):

    return len(set(arg))


if __name__ == '__main__':
    N = int(sys.argv[1])
    main(N, *map(int, sys.argv[2:]))
