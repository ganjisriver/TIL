TC = int(input())
for tc in range(1, TC+1):
    str1 = input()
    str2 = input()
    max_value = 0

    for i in range(len(str1)):
        cnt = 0
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                cnt += 1
            if max_value < cnt:
                max_value = cnt
    print(f'{tc} {max_value}')