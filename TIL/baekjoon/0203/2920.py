A = [1, 2, 3, 4, 5, 6, 7, 8]
B = [8, 7, 6, 5, 4, 3, 2, 1]

num_list = list(map(int, input().split()))

if num_list == A:
    print('ascending')
elif num_list == B:
    print('descending')
else:
    print('mixed')