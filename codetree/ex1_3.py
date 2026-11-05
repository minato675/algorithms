n, m = map(int, input().split())
points = [
    tuple(map(int, input().split())) for _ in range(m)
]  # [(1, 2), (2, 1), (2, 3), (2, 2), (3, 3), (4, 2), (3, 2), (4, 3)]

# Please write your code here.
arr = [[0 for _ in range(n)] for _ in range(n)]
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

for point in points:
    tmp = 0
    i, j = point[0] - 1, point[1] - 1
    arr[i][j] = 1
    for d in range(4):
        near_i = i + di[d]
        near_j = j + dj[d]
        if 0 <= near_i < n and 0 <= near_j < n:
            if arr[near_i][near_j] == 1:
                tmp += 1
        else:
            continue
    if tmp == 3:
        ans = 1
    else:
        ans = 0
    print(ans)
