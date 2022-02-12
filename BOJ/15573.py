n, m, k = map(int, input().split())
arr = [[0 for i in range(1010)] for j in range(1010)]
visited = [[False for i in range(1010)] for j in range(1010)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(1, n + 1):
    temp = [0] + list(map(int, input().split()))
    for j in range(1, m + 1):
        arr[i][j] = temp[j]

def in_range(x, y):
    return 0 <= x <= n and 0 <= y <= m + 1

def check(v):
    cnt = 0
    st = []

    st.append([0, 0])
    visited[0][0] = True
    while len(st) > 0:
        x = st[-1][0]
        y = st[-1][1]
        st.pop()

        if 1 <= x <= n and 1 <= y <= m:
            cnt += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not in_range(nx, ny) or visited[nx][ny] or arr[nx][ny] > v:
                continue

            st.append([nx, ny])
            visited[nx][ny] = True

    return cnt >= k

s = 0
e = 1000000
ans = 0
while s <= e:
    mid = (s + e) // 2

    visited = [[False for i in range(1010)] for j in range(1010)]

    if check(mid):
        ans = mid
        e = mid - 1
    else:
        s = mid + 1

print(ans)
