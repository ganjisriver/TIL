def lomuto(low, high):
    def partition(low, high):
        pivot = a[high]
        left = low

        for right in range(low, high):
            if a[right] < pivot:
                a[left], a[right] = a[right], a[left]
                left += 1
        a[left], a[high] = a[high], a[left]

        return left
    if low < high: # 리스트가 2개이상일 때 돌기 위한 조건
        pivot = partition(low, high)
        lomuto(low, pivot-1)
        lomuto(pivot+1, high)
    return
T = int(input())
for tc in range(1, T+1):
    a = list(map(int, input().split()))
    ans = lomuto(0, len(a)-1)
    print(*a)