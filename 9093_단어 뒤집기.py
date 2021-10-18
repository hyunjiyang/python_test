#try 1 : 리스트 이용
for _ in range(int(input())):
    arr = list(input().split())
    for i in arr:
        print(arr[::-1], end=" ")
      
#try 2 : stack 이용
for _ in range(int(input())):
    arr = input()+" "
    stack= []

    for i in arr:
        if i != " " :
            stack.append(i)
        else:
            while stack:
                print(stack.pop(), end="")
            print(" ", end="")
