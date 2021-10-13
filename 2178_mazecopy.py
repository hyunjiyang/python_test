from collections import deque

N,M = map(int,input().split())

#graph
graph = []
for _ in range(N):
    graph.append(list(map(int,input())))

#방문표시
visited = [[0]*M for _ in range(N)]

def BFS(x,y):
    #상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    #que = 좌표저장
    deq = deque()
    deq.append((x,y))
    visited[x][y] = 1

    while deq :
        x, y = deq.popleft() #거리값 계산 끝난 좌표 내보내기
        
        #상하좌우 탐색으로 위치까지 거리값 그래프에 입력
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<N and 0<=ny<M : #그래프 벗어나지않게 조절
                if graph[nx][ny] and not visited[nx][ny]:
                    print(deq)
                    deq.append((nx,ny)) #길 있는 좌표 추가
                    visited[nx][ny] = visited[x][y] + 1 #이전위치값+1로 경로계산

    return visited[N-1][M-1]

print(BFS(0,0))