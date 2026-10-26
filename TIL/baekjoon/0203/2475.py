num_list = list(map(int, input().split()))
num_sum = 0
for i in num_list:
    num_sum += i**2
    
ans = num_sum % 10

print(ans)