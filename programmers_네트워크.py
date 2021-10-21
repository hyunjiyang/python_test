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
