def SelectionSort(A, s):
    n = len(A)
    if s == n-1:
        return
    minimum = s
    for i in range(s, n):
        if A[minimum] > A[i]:
            minimum = i
    A[s], A[minimum] = A[minimum], A[s]

    SelectionSort(A, s+1)

A = [2, 4, 6, 1, 9, 8, 7, 0]
SelectionSort(A, 0)
print(A)