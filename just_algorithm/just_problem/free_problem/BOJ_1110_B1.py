N = input()
answer = N
cnt = 0
while True:
    if len(N) == 1:
        N = '0' + N
        temp = '0'+ N[-1]
    else:
        temp = str(int(N[0]) + int(N[1]))
    N = N[-1] + temp[-1]

    cnt += 1
    if int(N) == int(answer) :
        break


print(cnt)