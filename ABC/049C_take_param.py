import sys


def main():
    """引数を一つ取る"""
    args = sys.argv[1]
    S = args[::-1]

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

    print("YES" if can1 else "NO")


if __name__ == '__main__':
    main()
