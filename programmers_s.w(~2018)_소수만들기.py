#try1 : 중첩 for문을 없애는 방법은 없나?
from itertools import combinations as cb

def solution(nums):
    answer = 0
    num = list(map(sum,cb(nums,3)))
    for i in num:
        for n in range(2,i):
            if i%n == 0:
                break
            if n == i-1:
                answer+=1
        
    return answer
