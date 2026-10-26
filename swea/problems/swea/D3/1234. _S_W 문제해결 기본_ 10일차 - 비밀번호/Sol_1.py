for tc in range(1, 11):
    n, password = input().split()

    stack = []

    for num in password:
        if stack and stack[-1] == num:
            stack.pop()
        else:
            stack.append(num)

    print(f"#{tc} {''.join(stack)}")
