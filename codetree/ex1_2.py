commands = input()

x = 0
y = 0
dir = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
t = 0
tmp = 0
ans = -1

for char in commands:
    t += 1
    if char == "F":
        d = dir % 4
        x += dx[d]
        y += dy[d]
        if x == 0 and y == 0:
            tmp = 1
            break
    elif char == "L":
        dir += 1
    else:
        dir -= 1
if tmp == 1:
    ans = t

print(ans)
