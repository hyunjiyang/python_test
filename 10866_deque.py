#deque = 양방향 큐 / front push&pop rear push&pop

from sys import stdin
from collections import deque
input = stdin.readline

deq = deque()
for _ in range(int(input())):
    arr = list(input().split())
    if arr[0] == 'push_front' :
        deq.appendleft(arr[1])
    if arr[0] == 'push_back' :
        deq.append(arr[1])
    elif arr[0] == 'pop_front':
        print(-1 if len(deq)== 0 else deq.popleft())
    elif arr[0] == 'pop_back':
        print(-1 if len(deq)== 0 else deq.pop())
    elif arr[0] == 'size':
        print(len(deq))
    elif arr[0] == 'empty':
        print(1 if len(deq)==0 else 0)
    elif arr[0] == 'front':
        print(-1 if len(deq)==0 else deq[0])
    elif arr[0] == 'back':
        print(-1 if len(deq)==0 else deq[-1])
