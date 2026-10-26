T = int(input())

for tc in range(T):
    H, W, N = map(int, input().split())
    floor = 0
    num = 1
    for _ in range(N):
        floor += 1
        if floor > H:
            floor = 1
            num += 1
    floor = str(floor)
    num = str(num)

    if int(num) < 10 :
        num = '0'+ num

    print(floor+num)