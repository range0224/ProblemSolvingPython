n = int(input())
arr = [int(input()) for i in range(n)]

arr.sort(reverse=True)

ans = 0
for i in range(n):
    ans = max(ans, (i + 1) * arr[i])

print(ans)
