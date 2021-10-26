#try 1
def solution(numbers, target):
    answer = 0
    n = len(numbers)
    def dfs(index,value):
        if index == n :
            if value == target:
                nonlocal answer #전역변수 아닌 다른 scale 변수 참조
                answer += 1
            return
        else:
            dfs(index+1,value+numbers[index]) #각자 도는 트리
            dfs(index+1,value-numbers[index])   
    dfs(0,0)
    return answer
