# 입력받은 숫자 N까지의 합을 구하세요

N = int(input("숫자를 입력"))

total = 0
for i in range(1,N+1):
  total += i
print(f"1부터 {N}까지의 숫자의 합: {total}")