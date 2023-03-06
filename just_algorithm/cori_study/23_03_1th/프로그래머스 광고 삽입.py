from collections import deque
def change_time(time):
    hour, minute, second = time.split(":")
    second_time = int(hour)*3600 + int(minute)*60 + int(second)
    return second_time

def change_logs(logs):
    start_logs = []
    end_logs = []
    for i in range(len(logs)):
        start_time, end_time = logs[i].split("-")
        start_time = change_time(start_time)
        end_time = change_time(end_time)
        start_logs.append(start_time)
        end_logs.append(end_time)
    start_logs.sort()
    end_logs.sort()
    start_logs = deque(start_logs)
    end_logs = deque(end_logs)
    return start_logs, end_logs


def solution(play_time, adv_time, logs):
    answer = ''
    play_time = change_time(play_time)
    adv_time = change_time(adv_time)
    start_logs, end_logs = change_logs(logs)

    play_dict = dict()
    pointing = start_logs.popleft()
    if pointing != 0:
        play_dict[(0, pointing)] = 0

    cnt = 1
    while True:
        if start_logs and end_logs:
            if start_logs[0] > end_logs[0]:
                end_pop = end_logs.popleft()
                play_dict[pointing, end_pop] = cnt
                cnt -= 1
                pointing = end_pop
            elif start_logs[0] < end_logs[0]:
                start_pop = start_logs.popleft()
                play_dict[pointing, start_pop] = cnt
                pointing = start_pop
                cnt += 1
                pass
            else:
                start_logs.popleft()
                end_logs.popleft()
        elif end_logs and not start_logs:
            end_pop = end_logs.popleft()
            play_dict[pointing, end_pop] = cnt
            cnt -= 1
            pointing = end_pop
        else:
            play_dict[(pointing, play_time)] = cnt
            break
    time_list = [0 for _ in range(play_time+1)]
    accumulated_time_list = [0 for _ in range(play_time+1)]
    for key, value in play_dict.items():
        time_list[key[0]:key[1]] = [value for _ in range(key[1]-key[0])]
        accumulated_time_list[key[0]:key[1]] = [value for _ in range(key[1] - key[0])]


    return accumulated_time_list


def time_into_str(second_time):
    pass

play_time1 ="02:03:55"
adv_time1 = "00:14:15"
logs1 = ["01:20:15-01:45:14",
         "00:40:31-01:00:00",
         "00:25:50-00:48:29",
         "01:30:59-01:53:29",
         "01:37:44-02:02:30"]
custom_logs1 = ["01:20:15-01:45:14",
                "00:40:31-01:00:00",
                "00:25:50-01:55:29",
                "01:30:59-01:53:29",
                "01:37:44-02:02:30"]

play_time2 = "99:59:59"
adv_time2 = "25:00:00"
logs2 = ["69:59:59-89:59:59",
         "01:00:00-21:00:00",
         "79:59:59-99:59:59",
         "11:00:00-31:00:00"]

play_time3 = "50:00:00"
adv_time3 = "50:00:00"
logs3 = ["15:36:51-38:21:49",
         "10:14:18-15:36:51",
         "38:21:49-42:51:45"]

print(solution(play_time1, adv_time1, logs1))