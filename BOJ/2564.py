def get_min(x, value):
    if x == 1 or x == 3:
        return value
    elif x == 2:
        return n - value
    else:
        return m - value

m, n = map(int, input().split())
q = int(input())
arr = [list(map(int, input().split())) for i in range(q)]
x, y = map(int, input().split())
ud = [1, 2]
lr = [3, 4]

ans = 0
for i in range(q):
    if arr[i][0] == x:
        ans += abs(y - arr[i][1])
    elif x in ud and arr[i][0] in ud:
        ans += n + min(y + arr[i][1], (m - y) + (m - arr[i][1]))
    elif x in lr and arr[i][0] in lr:
        ans += m + min(y + arr[i][1], (n - y) + (n - arr[i][1]))
    else:
        ans += get_min(x, arr[i][1]) + get_min(arr[i][0], y)

print(ans)
