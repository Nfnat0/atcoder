import sys


def main(arg):
    """引数を一つ取る"""
    S = arg[::-1]

    values = ['dream', 'dreamer', 'erase', 'eraser']

    reversed_values = [value[::-1] for value in values]

    can1 = True
    i = 0
    while i < len(S):
        can2 = False
        for value in reversed_values:
            if S[i: i + len(value)] == value:
                can2 = True
                i += len(value)

        if not can2:
            can1 = False
            break

    return("YES" if can1 else "NO")


if __name__ == '__main__':
    main(sys.argv[1])
