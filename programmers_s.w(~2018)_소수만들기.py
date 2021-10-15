import itertools

def solution(nums):
    answer = []
    
    num = list(map(sum,itertools.combinations(nums,3)))
    for i in num:
        n=2
        while n < i :
            if i%n == 0:
                break
            
                
            
        
        #answer+=1
        
    return answer
