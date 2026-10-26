N = 5
M = 15
arr = [list(str(input())) for _ in range(N)]
ans = ''

for j in range(M):
    for i in range(N):
        if j >= len(arr[i]):
            continue
        else:
            ans += arr[i][j]

print(ans)