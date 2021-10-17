from collections import deque
from sys import stdin
input = stdin.readline


N = int(input())
deq = deque()

for _ in range(N):
    order= list(input().split())

    if order[0] == "push_front":
        deq.appendleft(order[1])
    elif order[0] == "push_back":
        deq.append(order[1])
    elif order[0] == "pop_front":
        print(-1 if len(deq)== 0 else deq.popleft())
    elif order[0] == "pop_back":
        print(-1 if len(deq)== 0 else deq.pop())
    elif order[0] == "size":
        print(len(deq))
    elif order[0] == "empty":
        print(1 if len(deq)== 0 else 0)
    elif order[0] == "front":
        if len(deq) == 0 :
            print(-1)
        else :
            print(deq[0])
    elif order[0] == "back":
        if len(deq) == 0 :
            print(-1)
        else :
            print(deq[-1])
