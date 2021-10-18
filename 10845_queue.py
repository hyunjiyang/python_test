#queue = rear push front pop

from sys import stdin
from collections import deque
input = stdin.readline

que = deque() 

for _ in range(int(input())):
    arr = list(input().split())
    if arr[0] == 'push' :
        que.append(arr[1])
    elif arr[0] == 'pop':
        print(-1 if len(que)== 0 else que.popleft())
    elif arr[0] == 'size':
        print(len(que))
    elif arr[0] == 'empty':
        print(1 if len(que)==0 else 0)
    elif arr[0] == 'front':
        print(-1 if len(que)==0 else que[0])
    elif arr[0] == 'back':
        print(-1 if len(que)==0 else que[-1])
