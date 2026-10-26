import day5_1


# 리스트에서 짝수만 출력하세요
a = day5_1.ans
for i in day5_1.ans: #for 함수에서 for i(몇번째 위치) in ans(리스트)
  if i % 2 == 0:
    print(i)