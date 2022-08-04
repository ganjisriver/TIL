test_num = int(input())
for i in range(test_num):
    b = input()
    year=int(b[:4])
    month=int(b[4:6])
    day=int(b[6:])
    print("#%d" %(i+1), end='')
    if month<1 or month>12:
        print(-1)
        continue
    if month in [1,3,5,7,8,10,12]:
        if day<1 or day>31:
            print(-1)
            continue
    if month == 2:
        if day<1 or day>28:
            print(-1)
            continue
    if month in [4,6,9,11]:
        if day<1 or day>30:
            print(-1)
            continue
    print("%.4d/%.2d/%.2d" %(year, month, day))
    # -1이 출력이 될 때, 옆에 몇번째인지 알려주는 #i가 나와야해서
    # 7번째 줄이 필요하다.
    # 또한 23줄의 %.4d처럼 정수의 자리수를 아는 것이 중요하다.