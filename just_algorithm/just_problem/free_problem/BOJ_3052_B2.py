A_set = set()
for i in range(10):
    N = int(input())
    a = N % 42
    A_set.add(a)
print(len(A_set))