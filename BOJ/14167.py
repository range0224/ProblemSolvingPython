import sys

sys.setrecursionlimit(100000)

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

n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
v = []

for i in range(n):
    for j in range(i + 1, n):
        v.append([i, j, (arr[i][0] - arr[j][0]) * (arr[i][0] - arr[j][0]) + (arr[i][1] - arr[j][1]) * (arr[i][1] - arr[j][1])])

v.sort(key=lambda x:x[2])

ans = 0
for i in range(len(v)):
    if find(v[i][0]) == find(v[i][1]):
        continue

    ans = max(ans, v[i][2])
    union_(v[i][0], v[i][1])

print(ans)
