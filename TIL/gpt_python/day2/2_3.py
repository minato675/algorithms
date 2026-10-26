# 숫자를 입력받아
# 짝수인지 홀수인지 출력하세요
num = int(input("숫자를 입력하세요: "))
ans = num%2
if ans == 0:
  print("짝수")
else:
  print("홀수")