n = 5 # 총 다섯줄의 입력이 주어진다. 
list_str = []
ans = ''
for n in range(n):
    word = input()
    list_str.append(word)
    for char in list_str:
        if len(char) == 0:
            continue
        else:
            ans += char.pop(0)
        print(ans)

# for word in list_str:
#     for n in word:
#         if word != "":
#             str = word.pop(0)
#             ans += str
#         else:
#             continue
# 세로로 읽은 순서대로 글자들을 출력한다. 이때, 글자들을 공백 없이 연속해서 출력한다. 
print(ans)