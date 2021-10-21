#DFS
n= int(input())
graph = [[0]*n for _ in range(n)]

for _ in range(int(input())):
    i,j = map(int,input().split())
    graph[i-1][j-1] = graph[j-1][i-1] = 1

def dfs(i):
    global answer
    visited[i] = 1
    for a in range(n):
        if graph[i][a] and not visited[a]:
            answer += 1
            dfs(a)

visited = [0 for _ in range(n)]
answer = 0
dfs(0)

print(len(answer))
