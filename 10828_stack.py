#stack = rear push rear pop

from sys import stdin
input = stdin.readline

stack = []

for _ in range(int(input())):
    arr = list(input().split())
    if arr[0] == 'push' :
        stack.append(arr[1])
    elif arr[0] == 'pop':
        print(-1 if len(stack)== 0 else stack.pop())
    elif arr[0] == 'size':
        print(len(stack))
    elif arr[0] == 'empty':
        print(1 if len(stack)==0 else 0)
    elif arr[0] == 'top':
        print(-1 if len(stack)==0 else stack[-1])
