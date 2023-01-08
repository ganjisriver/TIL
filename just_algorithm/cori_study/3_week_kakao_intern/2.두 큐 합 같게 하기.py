from collections import deque
def solution(queue1, queue2):
    큐1, 큐2 = deque(queue1), deque(queue2)
    합1, 합2 = sum(큐1), sum(큐2)
    큐길이대충두배 = 2*(len(큐1) + len(큐2))
    i = 0
    while True:
        if i > 큐길이대충두배:
            answer = -1
            break
        if 합1 == 합2:
            answer = i
            break
        if 합1 > 합2:
            뺀값1 = 큐1.popleft()
            큐2.append(뺀값1)
            합1 -= 뺀값1
            합2 += 뺀값1
        else:
            뺀값2 = 큐2.popleft()
            큐1.append(뺀값2)
            합1 += 뺀값2
            합2 -= 뺀값2
        i += 1

    return answer

