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

#bfs 최적화
from collections import deque
n,k = map(int,input().split())
deq = deque()
deq.append([n,0])
visited = [0]*100001

def bfs(n):
    while deq:
        v = deq.popleft()
        x, count = v[0],v[1]
        if visited[x]==0:
            visited[x]=1
            if x == k:
                return count
            count += 1
            if 0<=x-1:
                deq.append([x-1,count])
            if x+1<=k+1: #끝까지 갈 필요x k+1이 최대
                deq.append([x+1,count])
            if x*2<=k+1: #x*2가 k+1이상이면 작은게 이득.
                deq.append([x*2,count])
    return count

if n>=k: #최적화! 이 경우 뒤로 한칸씩 가는 방법 뿐
    print(n-k) 
else:
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
