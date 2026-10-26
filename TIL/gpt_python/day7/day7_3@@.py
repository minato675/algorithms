# 문자열에서 알파벳 개수를 출력하세요
# (공백 제외)

word = input('문장입력')

count = 0
for char in word:
    if char !=  " ":
        count += 1

ans = count
print(ans)


      