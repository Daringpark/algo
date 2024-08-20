import sys
sys.stdin = open('1063_output.txt')

king, pon, N = input().split()
move_dict = {'L' : [0,-1], 'R' : [0,1], 'T': [-1,0], 'B': [1,0],
             'LT': [-1,-1], 'RT': [-1,1], 'LB': [1,-1], 'RB': [1,1]}
chess_col = {'A' : 0, 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4, 'F' : 5, 'G' : 6, 'H' : 7}
def move():
    global king_pos
    global pon_pos
    for i in range(int(N)):
        king_move = move_dict[input()]
        new_king_pos_row = king_pos[0] + king_move[0]
        new_king_pos_col = king_pos[1] + king_move[1]
        if 0 <= new_king_pos_row < 8 and 0 <= new_king_pos_col < 8: # 이동 가능성 판단
            if new_king_pos_row == pon_pos[0] and new_king_pos_col == pon_pos[1]:
                # 폰이 있는 경우
                new_pon_pos_row = pon_pos[0] + king_move[0]
                new_pon_pos_col = pon_pos[1] + king_move[1]
                if 0 <= new_pon_pos_row < 8 and 0 <= new_pon_pos_col < 8:
                    king_pos = [pon_pos[0], pon_pos[1]]
                    pon_pos = [new_pon_pos_row, new_pon_pos_col]
                # 폰이 자리에 있다면, 그 방향으로 밀어내면서 같이 이동해야 됨.
            else:
                # 폰이 없으면서, 이동 가능
                king_pos = [new_king_pos_row, new_king_pos_col] # 새로운 위치로 교체
def position():
    king, pon = '', ''
    king += list(chess_col.keys())[king_pos[1]]
    king += str(8-king_pos[0])
    pon += list(chess_col.keys())[pon_pos[1]]
    pon += str(8-pon_pos[0])
    return f'{king}\n{pon}'
king_pos = [8-int(king[1]), chess_col[king[0]]]  # A1 col과 row로 이뤄짐
pon_pos = [8-int(pon[1]), chess_col[pon[0]]]
move()
print(position())