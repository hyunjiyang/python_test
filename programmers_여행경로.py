#try 1
from collections import defaultdict

def solution(tickets):
    routes = defaultdict(list)
    for key, value in tickets:
        routes[key].append(value)
    for key in routes.keys():
        routes[key].sort()

    visited = []
    stack = []

    def dfs(key):
        stack.append(key)
        while stack:
            key = stack[-1]
            if routes[key] != []:
                stack.append(routes[key].pop(0))
            else:
                visited.append(stack.pop())
        return visited[::-1]
    
    return dfs("ICN")

#try2 : visited를 안쓰고 싶다!!! -> testcase 실패... => 티켓의 KEY가 하나일 경우 문제 발생!!
from collections import defaultdict

def solution(tickets):
    routes = defaultdict(list)
    for key, value in tickets:
        routes[key].append(value)
    for key in routes.keys():
        routes[key].sort()
        
    stack = []

    def dfs(key):
        stack.append(key)
        while stack:
            key = stack[-1] 
            if routes[key] != []:
                stack.append(routes[key].pop(0))
            else:
                break # KEY가 1개면 티켓 1장만 사용하고 BREAK됨
        return stack[::]
    
    return dfs("ICN")
