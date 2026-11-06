n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.

arr = [0 for _ in range(10)]


for start, fin in segments:
    print(start)
    for j in range(start, fin + 1):

        arr[j] += 1
        print(j)
        print(arr)

ans = max(arr)

print(ans)
