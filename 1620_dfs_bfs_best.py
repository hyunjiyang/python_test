from collections import deque

n,m,v = map(int,input().split())

#구조 틀 만들기
graph = [[] for _ in range(n+1)] # 1*n+1 배열
visited_dfs = [0]*(n+1)
visited_bfs = [0]*(n+1)
deq = deque([v])
dfs_print = []
bfs_print = []

#그래프 채우기
for i in range(m):
    start, end = map(int, input().split())
    graph[start].append(end) #[],[123],[468]
    graph[end].append(start) #양방향

#함수만들기
def DFS(v):
    visited_dfs[v] = 1
    dfs_print.append(v)
    graph[v].sort() #순서대로 각 행 정렬
    for i in graph[v] :
        if visited_dfs[i] == 0 :
            DFS(i)

def BFS(v):
    while deq :
        a = deq.popleft()
        if visited_bfs[a] == 0:
            visited_bfs[a] = 1
            bfs_print.append(a)
            deq.extend(graph[a])

#실행함수
DFS(v)
BFS(v)

for i in dfs_print:
    print(i, end = " ")
print()
for i in bfs_print:
    print(i, end = " ")
            