N = int(input())
values = list(map(int, input().split()))

count = 0
flg = True
while flg:
    for i, _ in enumerate(values):
        if values[i] % 2 == 1:
            flg = False
            break
        else:
            values[i] /= 2
    if flg:
        count += 1

print(count)
