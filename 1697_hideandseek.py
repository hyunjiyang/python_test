#가장 빠른 건 BFS
from collections import deque

n,k = map(int,input().split())
deq = deque()
deq.append([n,0])
visited = [0 for _ in range(100001)]

def bfs(n):
    while deq:
        nx, t = deq[0][0], deq[0][1]
        if nx == k:
            break
        deq.popleft()
        visited[nx]=1
        if 0<=nx-1 and visited[nx-1]==0:
            deq.append([nx-1,t+1])
        if nx+1<=100000 and visited[nx+1]==0:
            deq.append([nx+1,t+1])
        if nx*2<=100000 and visited[nx*2]==0:
            deq.append([nx*2,t+1])
    return deq[0][1]

print(bfs(n))

# 재귀
n, k = map(int,input().split())

def recur(n,k):
    if n >= k :
        return n-k
    elif k==1:
        return 1
    elif k%2 == 0:
        return 1+min(recur(n,k-1),recur(n,k+1))
    else :
        return min(k-n, 1+recur(n,k//2))

print(recur(n,k))
