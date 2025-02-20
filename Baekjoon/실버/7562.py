from collections import deque

tc = int(input())

# 나이트의 이동 방향 왼쪽부터 시계방향으로
drdc = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]

def BFS(L, start_r, start_c, end_r, end_c):
	global visited
	
	queue = deque()
	queue.append((start_r, start_c))
	visited[start_r][start_c] = 1

	while queue:
		# 도착할 수 있다면?
		row, col = queue.popleft()
		
		if row == end_r and col == end_c:
			return visited[row][col]
		
		for dr, dc in drdc:
			new_row = row + dr
			new_col = col + dc
			
			if 0 <= new_row < L and 0 <= new_col < L:
				if not visited[new_row][new_col]:
					visited[new_row][new_col] = visited[row][col] + 1
					queue.append((new_row, new_col))
					
	# 2차원 배열에서의 모든 좌표는 도달 가능하다.
	return -1

for _ in range(tc):
	l = int(input())
	start_row, start_col = map(int, input().split())
	end_row, end_col = map(int, input().split())
	visited = [[0] * l for _ in range(l)]
	
	print(BFS(l, start_row, start_col, end_row, end_col) -1)