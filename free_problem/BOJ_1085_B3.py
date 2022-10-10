x, y, w, h = map(int, input().split())
min_value = 9999
a = abs(h-y)
b = abs(w-x)
min_value = min(a, b, x, y)
print(min_value)