from sys import stdin
from collections import deque
input = stdin.readline

deq = deque()
arr = []

n,k = map(int,input().split())

for i in range(1,n+1):
    deq.append(i)

while len(deq) > 0:
    deq.rotate(-k+1)
    arr.append(str(deq.popleft()))

print("<"+", ".join(arr)+">")
