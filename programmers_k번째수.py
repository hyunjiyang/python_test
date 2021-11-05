#try 1
def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        new = []
        s,e,n = commands[i]
        new.append(sorted(array[s-1:e]))
        answer.append(new[0][n-1])
    return answer
 
#try 2  = for문 commands 원소로 업그레이드! 
def solution(array, commands):
    answer = []
    for i in commands: 
        s,e,n = i
        answer.append(sorted(array[s-1:e])[n-1])
    return answer
  
#try 3 = 한줄코드! 이것이 파이썬
def solution(array, commands):
    return list(map(lambda x: sorted(array[x[0]-1:x[1]])[x[2]-1],commands))
