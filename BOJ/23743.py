import sys

sys.setrecursionlimit(300000)

par = [i for i in range(200010)]

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

n, m = map(int, sys.stdin.readline().rstrip().split())
v = [list(map(int, sys.stdin.readline().rstrip().split())) for i in range(m)]
arr = list(map(int, sys.stdin.readline().rstrip().split()))

for i in range(n):
    v.append([i + 1, n + 1, arr[i]])

v.sort(key=lambda x:x[2])

ans = 0
for i in range(len(v)):
    if find(v[i][0]) == find(v[i][1]):
        continue

    ans += v[i][2]
    union_(v[i][0], v[i][1])

print(ans)
