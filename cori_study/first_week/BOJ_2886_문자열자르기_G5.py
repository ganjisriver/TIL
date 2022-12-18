# # 시간 초과난 코드
# # 이진 탐색 냄새가 났지만, 그냥 풀었더니 역시 시간 초과 나옴
from collections import deque
row, column = map(int, input().split())

cnt = 0
table = deque(list(input()) for _ in range(row)) # 문자열 테이블 deque로 받아줌

while len(table) > 1: # 문자열 테이블을 계속 팝해줄거라 길이가 1될 때 까지 돌려줌
    table.popleft()
    string_table = [] # 문자열 중복검사를 위한 list 형태의 문자열 테이블 생성

    for j in range(column):
        string_sample = str() # string_table에 넣어줄 문자열 샘플 생성
        for k in range(len(table)):
            string_sample += table[k][j]
        string_table.append(string_sample)
    set_string_table = set(string_table) # 문자열 리스트를 통해서 set 씌워서 새로 만듬
    if len(string_table) != len(set_string_table): # 길이로 중복검사 틀리면 break하고 끝
        break
    else:
        cnt += 1

print(cnt)

# 이진탐색 출발
row, column = map(int, input().split())

table = [list(input()) for _ in range(row)]
start = 0
end = row - 1
while start <= end: # 시작지점이 end보다 커지면 탐색 종료
    mid = (start + end) // 2
    column_word_list = [] # 열로된 문자열 리스트 생성
    flag = True # flag를 통해서 왼쪽을 탐색할지 오른쪽을 탐색할지 결정
    for i in range(column):
        column_word = str() # 각각의 열로된 문자열
        for j in range(mid, row): # 오른쪽 탐색
            column_word += table[j][i]
        if column_word not in column_word_list: # 문자열 리스트안에 중복 없으면 계속 추가
            column_word_list.append(column_word)
        else: # 중복 있으면 반복문 끝내고 왼쪽 탐색 위해 end 변경
            end = mid - 1
            flag = False
            break
    if flag: # 중복 없으니 범위 좁히고 재탐색
        result = mid # 최종 결과가 mid 다음부터 중복이 발생하기 때문에 mid를 결과값으로 지정해두면서 갱신
        start = mid + 1

print(result)
