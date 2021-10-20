#try 1 : rotate 사용
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

#try2 :enumerate = 인덱스값 튜플로 함께 생성 , any() = 조건이 하나라도 해당되면 true출력

def solution(priorities, location):
    answer = 0
    queue =  [(i,p) for i,p in enumerate(priorities)]
    
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue) :
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                break
    return answer
