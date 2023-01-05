N = int(input())
object_list = []
q = []
answer = []
calculator = []
for _ in range(N):
    number = int(input())
    object_list.append(number)
idx = 0
for i in range(1, N+1):
    q.append(i)
    calculator.append('+')
    flag = True
    while flag:
        if idx >= N:
            break
        if not q:
            break
        if object_list[idx] == q[-1]:
            temp = q.pop()
            answer.append(temp)
            idx += 1
            calculator.append('-')
        else:
            break

if object_list == answer:
    for cal in calculator:
        print(cal)
else:
    print('NO')
