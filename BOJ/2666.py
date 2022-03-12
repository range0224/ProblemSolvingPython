n = int(input())
x, y = map(int, input().split())
m = int(input())
arr = [int(input()) for i in range(m)]

def recur(cur, a, b):
    if cur == m:
        return 0

    if arr[cur] <= a:
        return recur(cur + 1, arr[cur], b) + a - arr[cur]
    elif arr[cur] >= b:
        return recur(cur + 1, a, arr[cur]) + arr[cur] - b
    else:
        return min(recur(cur + 1, arr[cur], b) + arr[cur] - a, recur(cur + 1, a, arr[cur]) + b - arr[cur])

print(recur(0, min(x, y), max(x, y)))
