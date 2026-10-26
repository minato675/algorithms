num1 = int(input())
num2 = int(input())
num3 = int(input())

number = num1 * num2 * num3
str_number = str(number)
for i in range(10):
    count_num = str_number.count(str(i))
    print(count_num)
