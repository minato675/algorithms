def cal(a, b):
    ans = (a+b) * (a-b)
    return ans

a, b = map(int, input().split())

ans = cal(a, b)

print(ans)