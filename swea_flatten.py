import sys
sys.stdin = open('input(1).txt')

for tc in range(1, 11): # 
    N = int(input())
    box_height = list(map(int, input().split()))
    
    while N >= 0:
        max_height = 0
        min_height = 101
        for i in box_height:
            if i > max_height:
                max_height = i

        for j in box_height:
            if j < min_height:
                min_height = j
        
        if N == 0:
            break

        for k in range(len(box_height)):
            if box_height[k] == max_height:
                box_height[k] -= 1
                break
                
        for u in range(len(box_height)):
            if box_height[u] == min_height:
                box_height[u] += 1
                break
        
        
        N -= 1
    print(f'#{tc} {max_height-min_height}')




