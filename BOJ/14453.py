n = int(input())
arr = [""] + [input() for i in range(n)]
hps = "HPS"

prefix = [[0, 0, 0] for i in range(n + 1)]
for i in range(1, n + 1):
    for j in range(3):
        prefix[i][j] = prefix[i - 1][j]
        if arr[i] == hps[j]:
            prefix[i][j] += 1

ans = 0
for i in range(1, n):
    lmax = 0
    rmax = 0
    for j in range(3):
        lmax = max(lmax, prefix[i][j])
        rmax = max(rmax, prefix[n][j] - prefix[i][j])

    ans = max(ans, lmax + rmax)

print(ans)
