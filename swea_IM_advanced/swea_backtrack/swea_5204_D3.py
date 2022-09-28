def merge_sort(l_list):
    global cnt
    if len(l_list) == 1:
        return l_list

    left_half = l_list[:len(l_list)//2]
    right_half = l_list[len(l_list)//2:]
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    return merge(left, right)

def merge(left, right):
    global cnt
    result = [0]*(len(left) + len(right))
    l = r = idx = 0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result[idx] = left[l]
            l += 1
            idx += 1
        else:
            result[idx] = right[r]
            r += 1
            idx += 1
    while l < len(left):
        result[idx] = left[l]
        l += 1
        idx += 1
    while r < len(right):
        result[idx] = right[r]
        r += 1
        idx += 1
    if left[-1] > right[-1]:
        cnt += 1
    return result

T = int(input())
for tc in range(1, T+1):
    cnt = 0
    N = int(input())
    L_list = list(map(int, input().split()))
    ans = merge_sort(L_list)
    print(f'#{tc} {ans[N//2]} {cnt}')
