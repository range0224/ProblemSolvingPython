from collections import deque

k = int(input())
m, n = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]

dx = [[1, 0, -1, 0], [-2, -2, -1, -1, 1, 1, 2, 2]]
dy = [[0, 1, 0, -1], [-1, 1, -2, 2, -2, 2, -1, 1]]

que = deque()
visited = [[[False for i in range(k + 1)] for j in range(m)] for _ in range(n)]

def in_range(x, y, h):
    return 0 <= x < n and 0 <= y < m and 0 <= h <= k

d = 0
que.append([0, 0, 0])
visited[0][0][0] = True
while len(que) > 0:
    size = len(que)
    for _ in range(size):
        x, y, h = que[0][0], que[0][1], que[0][2]
        que.popleft()

        if x == n - 1 and y == m - 1:
            print(d)
            exit()

        for i in range(2):
            for j in range(len(dx[i])):
                nx = x + dx[i][j]
                ny = y + dy[i][j]
                nh = h + i

                if not in_range(nx, ny, nh) or visited[nx][ny][nh] or arr[nx][ny] != 0:
                    continue

                que.append([nx, ny, nh])
                visited[nx][ny][nh] = True

    d += 1

print(-1)
