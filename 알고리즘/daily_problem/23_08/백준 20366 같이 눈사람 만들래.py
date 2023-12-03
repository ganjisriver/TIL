import sys

input=sys.stdin.readline
N = int(input())
snow_list = list(map(int, input().split()))
snow_list.sort()


answer = 9999999999999
for i in range(N-3):
    for j in range(i+3, N):
        first_snowman = snow_list[i] + snow_list[j]
        start, end = i + 1, j - 1
        candi_ans = 999999999999
        while start < end:
            second_snowman = snow_list[start] + snow_list[end]
            if abs(first_snowman - second_snowman) < candi_ans:
                candi_ans = abs(first_snowman - second_snowman)

            if first_snowman > second_snowman:
                start += 1
            elif first_snowman < second_snowman:
                end -= 1
            else:
                answer = 0
                print(answer)
                exit(0)
        if candi_ans < answer:
            answer = candi_ans
print(answer)

