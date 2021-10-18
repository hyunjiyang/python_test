# try 1 : 괄호 수 체크
for _ in range(int(input())):
    arr = list(input())
    left = 0
    
    for i in arr:
        if i == "(" :
            left += 1
        elif i == ")":
            if left > 0:
                left -= 1
            else:
                left = -1 
                break
    print("YES" if left == 0 else "NO")

# try 2 : 스택
for _ in range(int(input())):
    arr = list(input())
    stack = []
    for i in arr:
        if i == "(" :
            stack.append(i)
        elif i == ")":
            if len(stack) > 0:
                stack.pop()
            else:
                stack.append(i)
                break
    print("YES" if len(stack) == 0 else "NO")
