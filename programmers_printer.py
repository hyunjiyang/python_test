from collections import deque
def solution(priorities, location):
    answer = 0
    deq = deque()
    for i in range(len(priorities)):
        if i == location:
            deq.append([priorities[i],1])
        else:
            deq.append([priorities[i],0])
            
    while deq:
        if max(deq,key= lambda x:x[0]) == deq[0] :
            if deq[0][1] == 1:
                deq.popleft()
                answer += 1
                break
            else:
                deq.popleft()
                answer += 1
        else : 
            deq.rotate(-1)
    return answer
