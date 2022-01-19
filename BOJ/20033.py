n = int(input())
arr = list(map(int, input().split()))

s = 1
e = n
ans = 1
while s <= e:
    mid = (s + e) // 2

    cnt = 0
    for i in range(n):
        if arr[i] >= mid:
            cnt += 1
        else:
            cnt = 0

        if cnt >= mid:
            break

    if cnt >= mid:
        ans = mid
        s = mid + 1
    else:
        e = mid - 1

print(ans)
