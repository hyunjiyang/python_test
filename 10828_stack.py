from sys import stdin
input = stdin.readline

N = int(input())
stack = list()

for _ in range(N):
    order= list(input().split())

    if order[0] == "push":
        stack.append(order[1])
    elif order[0] == "pop":
        if len(stack)== 0 :
            print(-1)
        else :
            print(stack.pop(-1))
    elif order[0] == "size":
        print(len(stack))
    elif order[0] == "empty":
        print(1 if len(stack)== 0 else 0)
    elif order[0] == "top":
        if len(stack) == 0 :
            print(-1)
        else :
            print(stack[-1])
