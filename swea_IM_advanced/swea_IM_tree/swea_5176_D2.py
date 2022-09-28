def inorder(n):
    global number
    if n <= N:                  # 전형적인 중위 순회코드
        inorder(n*2)            # 왼쪽으로 쭉쭉 내려감.
        tree_idx[n] = number    # 마지막 노드에서부터 number 1이 붙음.
        number += 1             # number를 적용하고 +1을 해줌. 다음번호
        inorder(n*2+1)          # 오른쪽 확인

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    tree_idx = [0]*(N+1)        # 인덱스 코드 생성
    number = 1                  # number의 초기값 설정
    inorder(1)                  # 함수 시작
    print(f'#{tc} {tree_idx[1]} {tree_idx[N//2]}')  # tree_idx[1]은 루트 값 / # tree_idx[N//2]는 N 노드의 부모노드 값


