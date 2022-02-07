import sys

sys.setrecursionlimit(100000)

n = int(input())
arr = [0] + list(map(int, input().split()))
v = [[] for i in range(n + 1)]
dp = [{} for i in range(n + 1)]

for i in range(n - 1):
    a, b = map(int, input().split())

    v[a].append(b)
    v[b].append(a)

def dfs(cur, prv):
    ret = 0

    if dp[cur].get(prv, -1) != -1:
        return dp[cur][prv]

    for nxt in v[cur]:
        if nxt == prv:
            continue

        ret = max(ret, dfs(nxt, cur))

    dp[cur][prv] = ret + arr[cur]
    return dp[cur][prv]

ans = -1
idx = 0
for i in range(1, n + 1):
    if ans < dfs(i, 0):
        ans = dfs(i, 0)
        idx = i

print(ans, idx)
