N, A, B = list(map(int, input().split()))

# 解き方1
result = 0
for i in range(1, N + 1):
    if A <= sum([int(v) for v in str(i)]) <= B:
        result += i

# 解き方2
result = 0
for i in range(1, N + 1):
    n = i
    total = 0
    while i > 0:
        total += i % 10
        i //= 10
    if A <= total <= B:
        result += n

print(result)
