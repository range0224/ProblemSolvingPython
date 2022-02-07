import sys

sys.setrecursionlimit(100000)

par = [i for i in range(10010)]

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

n, m, k = map(int, input().split())
v = [list(map(int, input().split())) for i in range(m)]

v.sort(key=lambda x:x[2])

ans = 0
cnt = 0
for i in range(m):
    if find(v[i][0]) == find(v[i][1]):
        continue

    ans += v[i][2] + cnt * k
    cnt += 1
    union_(v[i][0], v[i][1])

print(ans)
