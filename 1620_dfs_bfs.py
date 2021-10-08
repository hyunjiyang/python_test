from collections import deque

def DFS(v): #재귀로 구현
    visited[v] = True
    print(v, end= " ")
    for i in range(1,n+1):
        if Map[v][i] == 1 and visited[i] is False:
            DFS(i)

def BFS(v):
    deq = deque([])
    deq.append(v)
    visited_bfs[v] = True


    while deq : # q가 비어있지 않을동안(참일동안)
        v = deq.popleft()
        print(v, end= " ")
        for i in range(1,n+1):
            if Map[v][i] == 1 and visited_bfs[i] is False:
                deq.append(i)
                visited_bfs[i] = 1

n, m, v = map(int,input().split())
Map = [[0]*(n+1) for _ in range(n+1)] #경로 배열 초기화 / n+1*n+1 배열
visited = [False]*(n+1) #dfs 방문여부
visited_bfs = [False]*(n+1) #bfs 방문여부

for i in range(m): # [0][0][1][0][0]
    start, end = map(int,input().split())
    Map[start][end] = 1 #입력받은 경로값 1 만들기
    Map[end][start] = 1

DFS(v)
print() #한 줄 띄기 목적
BFS(v)
