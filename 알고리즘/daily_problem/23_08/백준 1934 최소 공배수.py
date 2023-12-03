def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcb(a, b):
    if b > a:
        a, b = b, a
    return (a * b) // gcd(a, b)
T = int(input())
for tc in range(T):
    A, B = map(int, input().split())
    if A == 1:
        print(B)
        continue
    elif B == 1:
        print(A)
        continue
    result = lcb(A, B)
    print(result)
