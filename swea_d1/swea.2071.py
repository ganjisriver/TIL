a = int(input())


for i in range(1, a+1):
    total = 0
    b = list(map(int, input().split()))
    for j in b:
        total +=j
    
    print(f'#{i} {round(total/len(b))}')


#이 문제에서는 정수화할 때, 반올림문제를 해결해야함.
#int는 내림이지만, round함수는 반올림이 가능한 함수다.