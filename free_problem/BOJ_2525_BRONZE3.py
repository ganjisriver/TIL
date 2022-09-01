hour, minutes = map(int, input().split())
time = int(input())
result = minutes+time
if result >= 60:
    N = result//60
    result = result -60*N
    hour = hour+N
    if hour >= 24:
        hour = hour - 24

print(f'{hour} {result}')