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
