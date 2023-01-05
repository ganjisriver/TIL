TC = int(input())                               # 테스트케이스
for tc in range(1, TC+1):
    V, E = map(int, input().split())            # V는 노드의 개수 E는 간선의 개수
    matrix = [[0]*(V+1) for _ in range(V+1)]    # 인접행렬 만들기

    for _ in range(E):
        start, end = map(int, input().split())  # start에서 end로 가는 경로 받아오기
        matrix[start][end] = 1                  # start에서 end로 일방향이므로, end start 역은 안 넣어준다.

    S, G = map(int, input().split())            # S는 시작지점 G는 도착지점

    stack = [S]                                 # S부터 시작해서 경로 구하기 위한 stack
    visited = []                                # S부터 시작해서 갈 수 있는 노드를 전부 넣어줄 예정

    while stack:                                # stack이 없을 때까지 while문 돌리기
        current = stack.pop()                   # current는 stack에서 하나 뽑는 거
        visited.append(current)                 # 양방향이면 current가 visited안에 있는지 여부를 판단해야하지만 일방향이라 상관없음

        for destination in range(V+1):          # current에서 갈 수 있는 노드를 stack에 추가해주는 작업
            if matrix[current][destination]:    # 마찬가지로 양방향이면 current가 visited안에 있는지 여부 판별해야하지만 일방향이라 상관없음
                stack.append(destination)
        if G in visited:                        # 효율을 위해 visited 안에 G가 들어간 순간 break하고 반복문을 종료한다.
            print(f'#{tc} 1')
            break

    if G not in visited:                        # 없으면 0 출력
        print(f'#{tc} 0')
