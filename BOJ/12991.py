n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

def check(x):
    cnt = 0
    for i in range(n):
        s = 0
        e = n - 1
        idx = -1
        while s <= e:
            mid = (s + e) // 2

            if a[i] * b[mid] <= x:
                idx = mid
                s = mid + 1
            else:
                e = mid - 1

        cnt += idx + 1

    return cnt >= m

s = 0
e = 1 << 60
ans = 0
while s <= e:
    mid = (s + e) // 2

    if check(mid):
        ans = mid
        e = mid - 1
    else:
        s = mid + 1

print(ans)
