# # ()(((()())(())()))(())
# # ******
# # # () 붙어있으면 *로 치환
# # # 나머지 (로 시작해서 )로 닫히는 가장 가까운 것을 찾고 사이에있는 *개수+1 더해주고 삭제 반복하면 답 나올듯


# TC = int(input())
# for tc in range(1, TC+1):
#     pipe_line = list(map(str, input()))
#     i = 0
#     cnt = 0
#     while i < len(pipe_line):

#         if pipe_line[i] == '(' and pipe_line[i+1] == ')':
#             pipe_line[i] = '.'
#             del pipe_line[i+1]
#         i += 1

#     for i in range(len(pipe_line)):
#         if pipe_line[i] == ')':
#             for j in range(i, 0, -1):
#                 if pipe_line[j] == '(':
#                     cnt += i-j
#                     del pipe_line[i]
#                     del pipe_line[j]

#     print(pipe_line)

def solution(s):
    
    char_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    num_list = []
    three_list = [0, 'one', 'two', 3, 4, 5, 'six', 7, 8, 9]
    four_list = ['zero', 1, 2, 3, 'four', 'five', 6, 7, 8, 'nine']
    five_list = [0, 1, 2, 'three', 4, 5, 6, 'seven', 'eight', 9]
    for num in range(10):
        num_list.append(int(num))
    answer = 0
    cnt = 0

    for i in range(len(s)-2):
        for j in range(len(three_list)):
            if s[i:i+3] == three_list[j]:
                s[i] = num_list[j]
                del s[i+2]
                del s[i+1]
    
    for i in range(len(s)-3):
        for j in range(len(four_list)):
            if s[i:i+4] == four_list[j]:
                s[i] = num_list[j]
                del s[i+3]
                del s[i+2]
                del s[i+1]
                
    for i in range(len(s)-4):
        for j in range(len(five_list)):
            if s[i:i+5] == five_list[j]:
                s[i] = num_list[j]
                del s[i+4]
                del s[i+3]
                del s[i+2]
                del s[i+1]
                
    answer = s
                
    
    
    return answer
solution('one4seveneight')