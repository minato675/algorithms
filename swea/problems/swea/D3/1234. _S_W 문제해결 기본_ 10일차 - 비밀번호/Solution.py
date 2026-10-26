T = 10
for tc in range(1, T + 1):
    N, M = map(str, input().split())  # 문자열의 길이
    N = int(N)  # 암호를 텍스트로
    num = [j for j in M]
    # print(num)
    dump = 1
    while dump == 1:
        dump = 0
        for i in range(N - 1):
            if num[i] == num[i + 1]:
                # print(num)
                # print(i)
                # print(N)
                del num[i : i + 2]
                N -= 2
                dump = 1
                break
            # else:
        if dump == 0:
            break
    # print(num)
    tmp = ""
    for ch in num:
        tmp += ch
    ans = tmp

    print(f"#{tc} {ans}")
