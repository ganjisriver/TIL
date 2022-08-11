TC = int(input())                               # 테스트 케이스
for tc in range(1, TC + 1):
    N, K = map(int, input().split())            # N은 부분집합의 개수, K는 N일 때의 부분집합의 합
    A = []
    is_sum_K = 0
    for num in range(1, 13):                    # A는 1부터 12까지의 정수 리스트를 만드는 것
        A.append(num)


    for i in range(1 << len(A)):                # 부분집합 만들기
        sub_list = []                           # 부분집합이 될 리스트
        total = 0                               # 부분집합들의 합을 담는 변수
        for j in range(len(A)):
            if i & (1 << j):
                sub_list.append(A[j])           # 부분집합을 만드는 sub_list 완성

        if len(sub_list) == N:                  # 부분집합의 개수가 N일 때,

            for u in sub_list:                  # 그 부분집합을 담은 sub_list의 합은 total 변수.
                total += u

            if total == K:                      # 그 부분집합의 합이 K와 일치할 때,
                is_sum_K += 1                   # 그 부분집합의 합의 개수를 세는 is_sum_K를 하나 증가시킴

    print(f'#{tc} {is_sum_K}')