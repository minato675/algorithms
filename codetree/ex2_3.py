n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.


# 중심점

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
tmp = []

for i in range(n):
    for j in range(m):
        # 중심좌표 기준으로 상하좌우 값 추출
        arr = []
        for a in range(4):
            dir = a
            tmp_i, tmp_j = i + di[dir], j + dj[dir]
            if 0 <= tmp_i < n and 0 <= tmp_j < m:
                arr.append(grid[tmp_i][tmp_j])
        arr.sort(reverse=True)

        tmp.append(arr[0] + arr[1] + grid[i][j])

ans = max(tmp)

print(ans)
