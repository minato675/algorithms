
problem = input()
list_ans = []

alphabet = ['a','b','c','d','e','f','g','h',
            'i','j','k','l','m','n','o','p','q','r',
            's','t','u','v','w','x','y','z']

for i in alphabet:
    ans = problem.find(i)
    list_ans.append(ans)

print(*list_ans)