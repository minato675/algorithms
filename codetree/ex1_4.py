n = int(input())
grid = [list(input()) for _ in range(n)]
k = int(input())

# Please write your code here.
di = [1, 0, -1, 0]
dj = [0, -1, 0, 1]
dir = (k - 1) // n
tmp_pos = (k - 1) % n
cnt = 0

# 초기 위치 설정
if dir == 0:
    i = 0
    j = tmp_pos
elif dir == 1:
    i = tmp_pos
    j = n - 1
elif dir == 2:
    i = n - 1
    j = n - 1 - tmp_pos
else:
    i = n - 1 - tmp_pos
    j = 0

# 레이저 진행
while 0 <= i < n and 0 <= j < n:
    cnt += 1
    if grid[i][j] == "/":
        if dir == 0:
            dir = 1
        elif dir == 1:
            dir = 0
        elif dir == 2:
            dir = 3
        else:
            dir = 2

    else:
        if dir == 0:
            dir = 3
        elif dir == 3:
            dir = 0
        elif dir == 2:
            dir = 1
        else:
            dir = 2

    i += di[dir]
    j += dj[dir]

print(cnt)
