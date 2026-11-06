n, m = map(int, input().split())

# Please write your code here.
arr = [[0 for _ in range(m)] for _ in range(n)]

i, j = 0, 0
dir = 0
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for index in range(n * m):
    char = chr(ord("A") + (index % 26))
    arr[i][j] = char
    tmp_i, tmp_j = i + di[dir % 4], j + dj[dir % 4]
    # print(tmp_i)
    # print(tmp_j)
    if not (0 <= tmp_i < n and 0 <= tmp_j < m):
        dir += 1
        # continue
    elif arr[tmp_i][tmp_j] != 0:
        dir += 1
        # continue
    i += di[dir % 4]
    j += dj[dir % 4]

for a in range(n):
    print(*arr[a])
