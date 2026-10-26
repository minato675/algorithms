# N , K = map(int, input().split())
N = 7
K = 3
numlist = list(range(1,N+1))
ans = []
word = ''
def rotate_list(list,n):
    dummy_list = []
    for i in list:
        dummy_list.append(None)

    for j in range(len(list)):
        dummy_list[j-n] = list[j]
        
    return dummy_list

for i in range(N):
    k = K
    if K > len(numlist):
        k = K % len(numlist)
    else:
        k = K
    numlist = rotate_list(numlist,k)    
    char = numlist.pop()
    ans.append(char)

for i in range(len(ans)-1):
    word += str(ans[i])+', ' 

word += str(ans[-1])

print(f'<{word}>')
