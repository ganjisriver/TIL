# import heapq
# from heapq import heappop, heappush, heapify
# T =int(input())
# for tc in range(T):
#     N = int(input())
#     file_size_list = list(map(int, input().split()))
#     dp = [0]*(N-1)
#     heapify(file_size_list)
#     for i in range(N-1):
#         min_size1 = heapq.heappop(file_size_list)
#         min_size2 = heapq.heappop(file_size_list)
#         result = min_size1 + min_size2
#         dp[i] = result
#         heappush(file_size_list, result)
#     answer= 0
#     for i in range(len(dp)):
#         answer += dp[i]
#     print(answer)

import sys
input=sys.stdin.readline
T=int(input())

for _ in range(T):
    N=int(input())

    cost_list=list(map(int,input().split()))

    dp=[[0]*N for _ in range(N)]

    for i in range(N-1):
        dp[i][i+1]=cost_list[i]+cost_list[i+1]      #두개씩 미리 더해줌

    prefix_sum=[0]*(N+1)
    prefix_sum[1]=cost_list[0]
    for i in range(2,N+1):
        prefix_sum[i]=prefix_sum[i-1]+cost_list[i-1]   #누적합 구해줌

    for i in range(2,N):                                                #길이가 3이상 부터 구해주기 위해 i=2부터 시작 ex)AB+C    -> 즉 i=2이면 3의 길이인 애들을 모두 구함
        for j in range(i,N):                                            #대각선 밑으로 내려가기 위한 for문
            min_value=10000000000
            for k in range(j-i,j):                                      #(1,4)가 있으면 (1,1)+(2,4), (1,2)+(3,4), (1,3)+(4,4) 중에 최소값을 구함
                min_value=min(min_value,dp[j-i][k]+dp[k+1][j])

            dp[j-i][j]=min_value+(prefix_sum[j+1]-prefix_sum[j-i])      #구한 최소값과 누적합을 더해줌

    print(dp[0][N-1])


