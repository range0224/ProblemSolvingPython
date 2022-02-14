import sys

n = int(sys.stdin.readline().rstrip())
arr = [-1] + [int(sys.stdin.readline().rstrip()) for i in range(n)] + [-1]

prefix = [0 for i in range(100010)]
suffix = [0 for i in range(100010)]

st = [0]
for i in range(1, n + 1):
    while arr[st[-1]] >= arr[i]:
        st.pop()

    prefix[i] = st[-1]
    st.append(i)

st = [n + 1]
for i in range(1, n + 1)[::-1]:
    while arr[st[-1]] >= arr[i]:
        st.pop()

    suffix[i] = st[-1]
    st.append(i)

ans = 0
for i in range(1, n + 1):
    ans = max(ans, arr[i] * (suffix[i] - prefix[i] - 1))

print(ans)
