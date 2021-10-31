from collections import deque

n, m, v = map(int,input().split())

#그래프 생성
Map = [[0]*(n+1) for _ in range(n+1)] #경로 배열 초기화 / n+1*n+1 배열
for _ in range(m): # [0][0][1][0][0]
    start, end = map(int,input().split())
    Map[start][end] = Map[end][start] = 1

#dfs준비
visited = [0]*(n+1)
#answer = []

#bfs준비
visited_bfs = [0]*(n+1) 
deq = deque([v])
#answer = []


def DFS(v): #재귀로 구현
    visited[v] = 1
    print(v, end= " ") #answer.append(i)
    for i in range(n+1):
        if Map[v][i] and not visited[i]:
            DFS(i)
    #return answer

def BFS(v):
    visited_bfs[v] = 1
    while deq : # q가 비어있지 않을동안(참일동안)
        v = deq.popleft()
        print(v, end= " ") #answer.append(v)
        for i in range(n+1):
            if Map[v][i] and not visited_bfs[i]:
                deq.append(i)
                visited_bfs[i] = 1

DFS(v) #print(DFS(v))
print() #한 줄 띄기 목적
BFS(v) #print(BFS(v))
