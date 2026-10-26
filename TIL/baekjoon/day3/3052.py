# 두 자연수 A와 B가 있을 때, A%B는 A를 B로 나눈 나머지 이다. 
# 예를 들어, 7, 14, 27, 38을 3으로 나눈 나머지는 1, 2, 0, 2이다. 

# 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 
# 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.

number_list = []
# 10회 반복
for i in range(10):
    n = int(input()) # 입력값 가져옴
    num = n % 42 # 42로 나눈 나머지 num 생성
    number_list.append(num) # 나머지 숫자들 리스트로 모음

number_set = set(number_list) # 리스트 세트화 진행 < 하면 중복값 제거
ans = len(number_set) # 요소 개수 구함
print(ans) #QED