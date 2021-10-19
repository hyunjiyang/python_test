def solution(bridge_length, weight, truck_weights):
    stack = [0]*bridge_length
    answer = 0
    
    while len(stack):
        stack.pop(0)
        answer += 1
        if truck_weights:
            if sum(stack) + truck_weights[0] <= weight:
                stack.append(truck_weights.pop(0))
            else: 
                stack.append(0)

    return answer
