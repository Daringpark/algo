
# 너무 하드코딩한 것 같은데

def solution(video_len, pos, op_start, op_end, commands):
    
    # 변수 저장
    time_list = [video_len, pos, op_start, op_end]
    for i in range(4):
        minute, second = map(int, time_list[i].split(':'))
        total = minute*60 + second
        if i == 0:
            total_second = total
        elif i == 1:
            pos_second = total
        elif i == 2:
            start_second = total
        else:
            end_second = total
    # 첫 시작이 저 안에 있다면?
    if start_second <= pos_second <= end_second:  
        pos_second = end_second
    
    # 버튼 조작
    for com in commands:
        # prev 이동
        if com == 'prev':
            # 안에 있다
            if 0 <= pos_second-10:
                pos_second -= 10
            # 밖에 있다
            else:
                pos_second = 0
        # next 이동
        else:
            # 안에 있으면
            if pos_second + 10 <= total_second:
                pos_second += 10
            else:
                pos_second = total_second
    
        # 이동 이후, start-end 사이에 있는지
        if start_second <= pos_second <= end_second:  
            pos_second = end_second
    
    # 결과 처리
    res_minute, res_second = pos_second//60, pos_second % 60
    result = ''
    # 분 처리
    if not (res_minute//10):
        result += f'0{res_minute}:'
    else:
        result += f'{res_minute}:'
    
    # 초 처리
    if not (res_second//10):
        result += f'0{res_second}'
    else:
        result += f'{res_second}'
        
    return result