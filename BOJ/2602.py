s = input()
arr = [input() for i in range(2)]
dp = [[[-1 for i in range(110)] for j in range(3)] for k in range(30)]

def recur(cur, x, y):
    ret = 0

    if cur == len(s):
        return 1

    if dp[cur][x][y] != -1:
        return dp[cur][x][y]

    for i in range(y, len(arr[0])):
        if s[cur] == arr[x ^ 1][i]:
            ret += recur(cur + 1, x ^ 1, i + 1)

    dp[cur][x][y] = ret
    
    return ret

print(recur(0, 0, 0) + recur(0, 1, 0))
