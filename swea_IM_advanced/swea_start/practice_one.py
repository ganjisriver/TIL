TC = int(input())

for tc in range(1, TC+1):
    A = input()

    for i in range(0, len(A), 7):
        result = (A[i:i+7])
        answer = int(result, 2)
        print(answer, end=' ')