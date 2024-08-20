
'''
2
2
0 0
0 100
1.0
4
0 0 400 400
0 100 0 100
1.0
'''

from heapq import heappush, heappop






T = int(input())

for tc in range(1, T+1):
    
    N = int(input())
    
    # 노드를 구해두기
    island_list = list()
    
    
    for _ in range(N): # N은 1e3이 최대
        x, y = map(int, input().split())
        island_list.append([x, y])
    
    graph = [[] for _ in range(N)] # 각 섬들은 번호를 가질 수 있다.
    
    # 각 노드들의 연결성 만들기 (무향 그래프)
    # 간선들의 길이를 구하는게 핵심
    
    Length_list = []
    
    
    
    
    price = 0
    E = float(input())
    # 길이 리스트를 저장
    for l in Length_list: # 각 간선의 가중치를 
        price += E*(l**2)
    price = round(price)
    
    
    print(f'#{tc} {price}')
    # 빗변을 타고 가는 것보다 그냥 직선으로 가는 경우가 더 빠르다.
    # 3 4 가 3 5나 4 5보다 더 빠르다.
    
    #  d = sqrt(a**2+b**2)
    
    
    
    
    
    







