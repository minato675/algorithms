import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

a = max(nums)
b = min(nums)

print(f"{b} {a}")