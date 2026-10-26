# import sys

# a, b = map(int, sys.stdin.readline().split())

# nums = list(map(int, sys.stdin.readline().split()))
# ans = []

# for i in range(a):
#     if nums[i] < b:
#         ans.append(nums[i])
#     else:
#         continue
        
# print(*ans)



a, b = map(int, input().split())

nums = list(map(int, input().split()))
ans = []

for i in range(a):
    if nums[i] < b:
        ans.append(nums[i])
    else:
        continue
        
print(*ans)

