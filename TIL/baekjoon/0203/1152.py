import sys

word_list = list(map(str, sys.stdin.readline().split()))
ans = 0
for _ in word_list:
    ans += 1

print(ans)