a = int(input())
total=0 # total을 for 안에 넣어야됨 print도 반복문의 영향을 받는 걸 고려 잘 해야됨.
for i in range(1,a+1):
    j = map(int, input().split())
    for y in j:
        
        if y % 2 == 1:
            total+=y
        else:
            continue
    print(f'#{i} {total}') # 반복문 영향 하에 들어가야함.