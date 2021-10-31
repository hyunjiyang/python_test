from collections import deque
n,m,v = map(int,input().split())

#그래프 [start][end]만들기
graph = [[] for _ in range(n+1)] # 1*n+1 배열
for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end) #[],[123],[468]
    graph[end].append(start) #양방향

#dfs준비
visited_dfs = [0]*(n+1)
answer_dfs = []

#bfs준비
visited_bfs = [0]*(n+1)
deq = deque([v])
answer_bfs = []


def DFS(v):
    visited_dfs[v] = 1
    answer_dfs.append(v)
    graph[v].sort() #순서대로 각 행 정렬
    for i in graph[v] :
        if visited_dfs[i] == 0 :
            DFS(i)

def BFS(v):
    while deq :
        a = deq.popleft()
        if visited_bfs[a] == 0:
            visited_bfs[a] = 1
            answer_bfs.append(a)
            deq.extend(graph[a])

#실행함수
DFS(v)
BFS(v)

for i in dfs_print:
    print(i, end = " ")
print()
for i in bfs_print:
    print(i, end = " ")
            
