par = [i for i in range(1000010)]
rnk = [0 for i in range(1000010)]
gnum = [0 for i in range(1000010)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
sum = 0

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

def find(x):
    if par[x] == x:
        return x
    else:
        return find(par[x])

def union_(a, b):
    global sum

    a = find(a)
    b = find(b)

    if a == b:
        return

    sum -= gnum[a] + gnum[b]

    if rnk[a] < rnk[b]:
        gnum[b] ^= gnum[a]
        par[a] = b
        sum += gnum[b]
    elif rnk[a] > rnk[b]:
        gnum[a] ^= gnum[b]
        par[b] = a
        sum += gnum[a]
    else:
        gnum[b] ^= gnum[a]
        par[a] = b
        rnk[b] += 1
        sum += gnum[b]

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
v = []

for i in range(n):
    for j in range(m):
        v.append([arr[i][j], i, j])
        gnum[i * m + j] = arr[i][j]

v.sort(key=lambda x: -x[0])

ans = 0
for i in range(len(v)):
    x = v[i][1]
    y = v[i][2]
    sum += v[i][0]

    for j in range(4):
        nx = x + dx[j]
        ny = y + dy[j]

        if not in_range(nx, ny) or arr[nx][ny] < arr[x][y]:
            continue

        union_(x * m + y, nx * m + ny)

    ans = max(ans, sum)

print(ans)
