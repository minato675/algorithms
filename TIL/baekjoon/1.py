arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]
new_arr = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
n = 5
m = 3
for i in range(n):
    for j in range(m):
        new_arr[i][j] = (arr[i][j*((i+1)%2)+(-j-1)*(i%2)])
    print(*new_arr[i])