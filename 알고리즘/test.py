import math
A, B, V = map(int, input().split())
X = (V - A) / (A - B) + 1
print(math.ceil(X))

