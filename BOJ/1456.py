a, b = map(int, input().split())

prime = [True for i in range(10000010)]
cnt = 0

for i in range(2, 10000001):
    if not prime[i]:
        continue

    j = i * i
    while j <= b:
        if j >= a:
            cnt += 1
        j *= i

    for j in range(i * i, 10000010, i):
        prime[j] = False

print(cnt)
