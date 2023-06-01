import heapq
N = int(input())
people = list(map(int, input().split()))
time_list = [0 for _ in range(N)]
heapq.heapify(people)
for i in range(N):
    person = heapq.heappop(people)
    if i == 0:
        time_list[0] = person
    else:
        time_list[i] = time_list[i-1] + person

hap = sum(time_list)
print(hap)

