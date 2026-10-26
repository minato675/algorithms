T = int(input())
for tc in range(T):
    ans = ''
    n, word = map(str, input().split())
    n = int(n)

    for char in word:
        ans += char*n

    print(ans)