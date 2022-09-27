T = int(input())
for tc in range(1, T+1):
    OX = input()
    answer = 0
    cnt = 0
    hap = 0
    for i in range(len(OX)):
        if OX[i] == 'X':
            answer += hap
            cnt = 0
            hap = 0
        elif OX[i] == 'O':
            cnt += 1
            hap += cnt
        if i == len(OX) - 1:
            answer += hap
    print(answer)