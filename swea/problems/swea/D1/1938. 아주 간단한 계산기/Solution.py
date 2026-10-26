a, b = map(int, input().split())

arr = []
arr.append(a + b)
arr.append(a - b)
arr.append(a * b)
arr.append(a // b)

for char in arr:
    print(char)
