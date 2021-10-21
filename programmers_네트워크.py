#DFS
def solution(n, computers):
    answer = 0
    def dfs(i):
        visited[i] = 1
        for a in range(n):
            if computers[i][a] == 1 and visited[a] == 0 :
                dfs(a)
                
    visited = [0 for i in range(n)]
    for i in range(n):
        if visited[i] == 0 :
            dfs(i)
            answer +=1

    return answer

#BFS
from collections import deque

def solution(n, computers):
    answer = 0
    def bfs(i):
        deq = deque()
        deq.append(i)
        while deq:
            i = deq.popleft()
            visited[i] = 1
            for a in range(n):
                if computers[i][a] == 1 and visited[a] == 0 :
                    deq.append(a)
                
    visited = [0 for i in range(n)]
    for i in range(n):
        if visited[i] == 0 :
            bfs(i)
            answer +=1

    return answer
