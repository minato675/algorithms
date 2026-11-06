n, t = map(int, input().split())  # n은 한변의 숫자 개수 / t는 돌리는 횟수

l = list(map(int, input().split()))
r = list(map(int, input().split()))
d = list(map(int, input().split()))

# Please write your code here.

for _ in range(t):
    tmp_l = l[n - 1]
    tmp_r = r[n - 1]
    tmp_d = d[n - 1]

    for i in range(n - 1, 0, -1):
        l[i] = l[i - 1]
        r[i] = r[i - 1]
        d[i] = d[i - 1]

    l[0] = tmp_d
    r[0] = tmp_l
    d[0] = tmp_r

print(*l)
print(*r)
print(*d)
