n = int(input())
values = sorted(list(map(int, input().split())), reverse=True)
print(sum(values[::2]) - sum(values[1::2]))
