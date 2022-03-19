from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
x, y, dir = map(int, input().split())
ex, ey, edir = map(int, input().split())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
change_dir = [0, 1, 3, 0, 2]

x -= 1
y -= 1
dir = change_dir[dir]

ex -= 1
ey -= 1
edir = change_dir[edir]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

que = deque()
visited = [[[False for i in range(5)] for j in range(m)] for i in range(n)]

d = 0
que.append([x, y, dir])
visited[x][y][dir] = True
while len(que) > 0:
    size = len(que)
    for _ in range(size):
        x, y, dir = que[0][0], que[0][1], que[0][2]
        que.popleft()

        if x == ex and y == ey and dir == edir:
            print(d)
            exit()

        for i in range(1, 4):
            nx = x + i * dx[dir]
            ny = y + i * dy[dir]

            if not in_range(nx, ny) or arr[nx][ny] == 1:
                break

            if visited[nx][ny][dir]:
                continue

            que.append([nx, ny, dir])
            visited[nx][ny][dir] = True

        ndir = (dir + 1) % 4
        if not visited[x][y][ndir]:
            que.append([x, y, ndir])
            visited[x][y][ndir] = True

        ndir = (dir + 3) % 4
        if not visited[x][y][ndir]:
            que.append([x, y, ndir])
            visited[x][y][ndir] = True

    d += 1
