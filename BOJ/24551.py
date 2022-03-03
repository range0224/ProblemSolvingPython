arr = [11, 111, 11111, 1111111, 11111111111, 1111111111111, 11111111111111111]

n = int(input())
ans = n

def recur(cur, mul, cnt):
    global ans

    if mul > n:
        return

    if cur == 7:
        if cnt % 2 == 0:
            ans -= n // mul
        else:
            ans += n // mul

        return

    recur(cur + 1, mul * arr[cur], cnt + 1)
    recur(cur + 1, mul, cnt)

recur(0, 1, 0)

print(ans)
