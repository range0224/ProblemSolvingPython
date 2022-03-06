from collections import deque

def bfs(x, y):
    que = deque()
    cnt = 0

    que.append([x, y])
    visited[x][y] = True
    while len(que) > 0:
        x, y = que[0][0], que[0][1]
        que.popleft()

        cnt += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not(0 <= nx < n and 0 <= ny < m) or arr[nx][ny] == 0 or visited[nx][ny]:
                continue

            que.append([nx, ny])
            visited[nx][ny] = True

    return cnt

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
visited = [[False for i in range(m)] for j in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

cnt = 0
ans = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0 or visited[i][j]:
            continue

        cnt += 1
        ans = max(ans, bfs(i, j))

print(cnt)
print(ans)
