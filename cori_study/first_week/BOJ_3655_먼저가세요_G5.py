tc = int(input())
for T in range(tc):
    waiting_people_number = int(input()) # 기다리는 사람 수
    waiting_people = list(input()) # 기다리는 사람 리스트로 변환

    # 그룹의 중복 여부를 확인하기 위한 set()
    waiting_people_group = set()

    # 그룹 딕셔너리에 들어갈 항목 {특정 그룹의 문자열: [같은 그룹 사람들의 초기 위치]}
    waiting_group_info = dict()

    # 그룹 딕셔너리에 정보를 담는 과정
    for i in range(waiting_people_number):
        current_person = waiting_people[i] # 현재 내가 보고 있는 사람 ex) 'A'

        # 내가 이미 딕셔너리에 넣은 집단이냐 아니냐에 따라 딕셔너리에 넣는 방식이 달라짐
        if current_person not in waiting_people_group: # 처음 보는 그룹인 경우
            waiting_people_group.add(current_person) # 중복 체크를 위해 set에 넣어줌
            waiting_group_info[current_person] = [i] #해당 그룹을 key로 갖고, 현재 위치를 포함하는 리스트를 value로 넣어준다.

        else: #이미 봤던 집단인 경우
            for key in waiting_group_info: # 딕셔너리 안에 key값을 돌아다닌다.
                if current_person == key: # 내가 속한 집단일 경우가 맞는다면
                    waiting_group_info[key].append(i) # 그 집단의 리스트에 현재 사람의 인덱스를 추가해 준다.
                    break # 이미 찾았으니 더 돌필요 없이 break 선언

    # 현재까지 완료하면 예제 입력 기준 waiting_group_info의 상태
    #1 {'A': [0, 1, 3], 'B': [2, 4, 5]}
    #2 {'A': [0, 3, 4], 'b': [1, 5, 7], '9': [2], '2': [6, 9], 'C': [8]}

    pre_waiting_time = 0 # 양보 하기 전 모든 사람들의 기다리는 시간
    changed_time = 0     # 양보를 하고 걸리는 모든 사람들의 기다리는 시간

    # 딕셔너리를 돌면서 시간을 구하는데, 마지막 사람을 기준으로 인덱스 하나 차이당 5만큼의 시간이 소요된다.
    # 결국 모두가 양보하게 되면, 결론적으로 같은 그룹끼리 붙어있는 형태가 된다.

    for key in waiting_group_info: # 같은 집단별로 반복문 돈다.
        if len(waiting_group_info[key]) == 1: # 집단이 혼자일 경우 기다리는 것이 필요 없기 때문에, 넘긴다.
            continue
        last_idx = waiting_group_info[key][-1] # 마지막 사람을 기준으로 기다리는 시간이 정해지기 때문에, 따로 저장
        waiting_group_list = waiting_group_info[key] # 같은 집단의 인덱스 리스트를 변수 지정

        for i in range(len(waiting_group_list)-1): # 이제 집단 내에서 마지막 사람을 제외하고 반복문을 돈다.

            # 양보하기 전에는 마지막 사람을 기준으로 반복문을 도는 사람들의 인덱스를 빼주면 원래 기다리는 시간이 나온다.
            pre_waiting_time += last_idx - waiting_group_list[i]

            # 양보한 후에는 모든 그룹이 붙어 있기 때문에, 마지막 사람과의 거리만 구하면서 더해주면 양보한 경우의 기다리는 시간이 된다.
            changed_time += len(waiting_group_list)-1 - i

    #양보 하기 전 기다리는 시간에서 양보한 후의 기다리는 시간을 빼주고 5를 곱하면 절약된 기다리는 시간이 나온다.
    result = 5*(pre_waiting_time - changed_time)
    print(result)



