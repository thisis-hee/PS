from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    truck_weights=deque(truck_weights)
    bridge = deque([0]*bridge_length)
    second = 0
    
    current_weight = 0
    while truck_weights:
        second+=1
        current_weight -= bridge.popleft()
        
        
        if current_weight + truck_weights[0] <= weight:
            current_weight+=truck_weights[0]
            bridge.append(truck_weights.popleft())
        
        else:
            bridge.append(0)
    
    second+=bridge_length
            
    answer = second
    
    return answer