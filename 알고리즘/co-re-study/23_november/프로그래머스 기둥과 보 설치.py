def solution(n, build_frame):
    answer = [[]]

    installed_index = set()
    status = [[[0, 0] for _ in range(n + 2)] for _ in range(n + 2)]

    for frame_info in build_frame:
        if not index_check(frame_info, installed_index, status):
            continue

    return answer


def index_check(frame_info, installed_index, status):
    frame_index = [frame_info[1], frame_info[0]]
    frame_kind, frame_act = frame_info[2], frame_info[3]
    if frame_index in installed_index:
        if status[frame_index[0]][frame_index[1]][frame_kind]:
            if not frame_act:
                status[frame_index[0]][frame_index[1]][frame_kind] = 0
                installed_index.pop(frame_index)
                return True
    else:
        if not status[frame_index[0]][frame_index[1]][frame_kind]:
            if frame_act:
                if frame_kind == 0:
                    # 기둥을 설치할 때, 고려 사항
                    # 1차 바닥인지
                    # 보 위에 있는지 또는 아래에 기둥이 있는지
                    if frame_index[0] == 0:
                        build()
                    elif status[frame_index[0]][frame_index[1]][1] or status[frame_index[0]][frame_index[1] + 1][1]:
                        build()
                    elif status[frame_index[0] - 1][frame_index[1]][0]:
                        build()
                else:
                    # 보를 설치할 때 고려 사항
                    # 1차 양 끝에 하나라도 기둥이 있는지
                    # 2차 양 끝에 둘다 보가 있는지
                    if status[frame_index[0] - 1][frame_index[1]][1]

                return True
    return False


def build():
    return





