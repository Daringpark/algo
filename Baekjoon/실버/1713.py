
# BOJ 1713 후보 추천하기
# 21 33 22 01

def remove_photo():
    min_recommend = 1000
    goal = []

    # 프레임에 있는 사진의 recommend를 먼저 걸러야 된다.
    for number in frame:
        if min_recommend > recommend_dict[number]:
            min_recommend = recommend_dict[number]
            goal = [number]
        # 같을 때가 필요해
        elif min_recommend == recommend_dict[number]:
            goal.append(number)

    # 그 값 처리
    recommend_dict[goal[0]] = 0
    idx = frame.index(goal[0])
    frame.pop(idx)

# 사진 틀은 20 이하
N = int(input())

# 전체 학생의 투표 횟수 << 1000번 이하
M = int(input())
vote = list(map(int, input().split()))

# 사전 구성
recommend_dict = dict()
for i in range(1, 101):
    recommend_dict.setdefault(i, 0)
frame = []

# 직접 리스트 순회를 통해서 프레임을 추가할지 말지를 정한다.
for item in vote:
    # 프레임에 이미 들어있다면
    if item in frame:
        recommend_dict[item] += 1
        # time_increase()

    # 프레임에 들어 있지 않을 때,
    else:
        # 프레임의 길이를 초과할 때, (새로 넣을 때)
        if len(frame) == N:
            remove_photo()
            recommend_dict[item] += 1
            frame.append(item)

        # 길이를 초과하지 않을 때 (그냥 넣어주기)
        else:
            # 우선 추가
            frame.append(item)
            # 해당 번호 추천수 올리기
            recommend_dict[item] += 1
            # time_increase()
    # print(frame)

# 출력단 오름차순으로 정렬 후 원소 출력
frame.sort()
print(*frame)


'''
3
9
2 1 4 3 5 6 2 7 2

2 6 7
'''