import heapq
def solution(food_times, k):
    answer = 0
    all_food_time = 0
    last_time = 0
    food_heap = []
    clear_food_index = set()
    for i in range(len(food_times)):
        food_heap.append((food_times[i], i))
        all_food_time += food_times[i]

    if k >= all_food_time:
        return -1

    heapq.heapify(food_heap)
    last_min = 0
    while True:
        left_food_num = len(food_heap)
        food_min = food_heap[0][0]
        left_food_min = food_min - last_min
        cycle = (k / (last_time + left_food_min*left_food_num))
        if cycle > 1:
            last_time += left_food_min*left_food_num
            while True:
                food_min = int(str(food_min)) # 복사에서 참조한걸 방지하기 위한 로직
                if food_min == food_heap[0][0]:
                    clear_food_index.add(food_heap[0][1])
                    heapq.heappop(food_heap)
                    last_min = int(str(food_min))
                else:
                    break
        else:
            for i in range(len(food_times)):
                if last_time == k:
                    # if i != len(food_times)-1:
                    return i + 1
                    # else:
                    #     return 1
                if i in clear_food_index:
                    continue
                else:
                    last_time += 1
                    if last_min >= food_times[i]:
                        clear_food_index.add(i)
                    food_times[i] = food_times[i] - 1

    return answer


food_times = [3, 1, 2]
k = 5
print(solution(food_times, k))