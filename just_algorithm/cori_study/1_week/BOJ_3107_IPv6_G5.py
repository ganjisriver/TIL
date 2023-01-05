# 입력 받았을 때, 리스트 안에 빈 문자열이 2개 이상 있으면 끝까지 0000으로 이루어졌음을 의미
# 빈 문자열이 한개면 그 문자열 자리에 리스트 길이가 8개 될 떄 까지 '0000'을 채워주면 됨

from collections import deque

string_list = deque(map(str, input().split(':'))) # ':' 기준으로 deque 생성

zero_count = 0 # string_list안에 나오는 빈 문자열의 개수를 의미
# ':' 기준으로 나눴기 때문에, 생략된 '0000'이 가운데 있으면 빈 문자열 1개 '0000'이 리스트 끝까지 나아가면 빈 문자열이 2개 나옴

zero_idx = [] # 빈 문자열의 인덱스를 찾기 위한 리스트 길이 0~2개

# 빈 문자열 여부 파악 + 앞부분의 생략된 '0'을 넣어주기 위한 작업
for i in range(len(string_list)):
    if string_list[i] == '':
        zero_count += 1 # 빈 문자열 개수 확인
        zero_idx.append(i) # 빈 문자열 인덱스 찾기
    else:
        while len(string_list[i]) < 4: # 빈 문자열이 아닌 곳은 앞 부분에 0 채워주기
            string_list[i] = '0' + string_list[i]

# 빈 문자열이 없으면 앞부분에 0만 채워주면 되기 떄문에 pass
if zero_count == 0:
    pass

# zero_count가 한개면 생략된 '0000'이 리스트 중간에 있다는 의미
elif zero_count == 1:
    zero_space = zero_idx[0] # 빈 문자열의 인덱스를 특정
    while len(string_list) < 8:
        string_list.insert(zero_space+1, '0000') # 리스트가 8개가 될 떄까지 생략된 '0000'을 채워준다.
    string_list[zero_space] = '0000' # 마지막으로 빈 문자열을 0000으로 바꿔주면 끝

# 빈 문자열이 2개 인 경우
elif zero_count == 2 and len(string_list) <= 8:

    # 빈 문자열을 0000으로 바꿔준 후에 부족한 길이만큼 0000을 추가로 채워준다.
    string_list[zero_idx[0]] = '0000'
    string_list[zero_idx[1]] = '0000'

    # 빈 문자열이 2개인 경우 리스트 한쪽 끝부분이 0000이기 때문에 끝 부분에 추가해주면 됨
    if zero_idx[0] == 0:
        while len(string_list) < 8:
            string_list.appendleft('0000')
    else:
        while len(string_list) < 8:
            string_list.append('0000')

#예외 케이스 ::1:2:3:4:5:6:7 or 1:2:3:4:5:6:7:: 처럼 끝부분에 :한개만 써도 될 것 같은데 ':'가 2개 되어있어서 한개 삭제해줘야됨
else: # 즉 이 경우는 zero_count가 2개이면서 string_list의 길이가 9개인 상태
    if zero_idx[0] == 0:
        string_list[zero_idx[1]] ='0000'
        string_list.popleft()
    else:
        string_list[zero_idx[0]] ='0000'
        string_list.pop()

answer = ':'.join(string_list)

print(answer)



