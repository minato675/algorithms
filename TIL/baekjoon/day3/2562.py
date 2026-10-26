n = 9

number_list = []

for i in range(9):
    num = int(input())
    number_list.append(num)

ans = max(number_list)

ans2 = number_list.index(ans)

print(f'{ans} {ans2+1}')