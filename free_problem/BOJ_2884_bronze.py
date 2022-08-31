hour, minutes = map(int, input().split())

minutes = minutes - 45
if minutes < 0 :
    minutes = 60 + minutes
    hour = hour - 1
    if hour == -1:
        hour = 23

print(f'{hour} {minutes}')
