# "OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다. 
# 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다. 
# 예를 들어, 10번 문제의 점수는 3이 된다.

# "OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.

# OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.


# 첫째 줄에 테스트 케이스의 개수가 주어진다. 
# 각 테스트 케이스는 한 줄로 이루어져 있고, 길이가 0보다 크고 80보다 작은 문자열이 주어진다. 
# 문자열은 O와 X만으로 이루어져 있다.

n = int(input())

for i in range(n): # 테스트 횟수만큼 반복
    score = 0 # 처음 배점 설정
    score_list = [] # 점수표 생성   
    case = input() # 입력값을 case로 받음
    for char in case: # case의 알파벳 요소별로 반복
        if char == 'X': # char 이 X 라면
            score = 0 # 점수를 0으로 초기화
            score_list.append(score) # 점수를 점수표에 추가
            continue # 다시 다음번 문제 진행
        score += 1 # 맞았으니 점수 1 추가 << 연속정답일시 계속 추가배점
        score_list.append(score) # 점수를 점수표에 추가 <<< 반복문 char ~~ 끝

    total_score = sum(score_list) # 점수표에 있는 점수 합산
    print(total_score) # 합산 점수 출력 <<< 반복문 i ~~ 끝
