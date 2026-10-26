# 숫자를 계속 입력받아
# 0이 입력되면 종료하고
# 입력한 숫자의 개수를 출력하세요
nums = []

while True:
  a = int(input())
  nums.append(a)
  if a == 0:
    break
nums.remove(0)
print(nums)
ans = len(nums)
print(ans)
