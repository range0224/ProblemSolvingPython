import sys

sys.setrecursionlimit(1000000)

par = [i for i in range(1010)]

def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def union_(a, b):
    a = find(a)
    b = find(b)

    par[a] = b

n, m = map(int, input().split())
gender = [0] + list(map(str, input().split()))
v = []

for i in range(m):
    a, b, c = map(int, input().split())

    if gender[a] == gender[b]:
        continue

    v.append([a, b, c])

v.sort(key=lambda x:x[2])

ans = 0
cnt = 0
for i in range(len(v)):
    if find(v[i][0]) == find(v[i][1]):
        continue

    union_(v[i][0], v[i][1])
    ans += v[i][2]
    cnt += 1

if cnt == n - 1:
    print(ans)
else:
    print(-1)
