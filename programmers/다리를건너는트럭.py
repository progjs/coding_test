# https://programmers.co.kr/learn/courses/30/lessons/42583
# 다리를 지나는 트럭

def solution(bridge_length, weight, truck_weights):
    from collections import deque
    
    answer, idx = 0, 0
    bridge, w = deque(), 0
    trucks = deque(truck_weights)
    
    while trucks:
        if bridge and answer == bridge[0][1]:
            bridge.popleft()
            w -= trucks.popleft()
        if idx < len(truck_weights):
            if w+truck_weights[idx] <= weight:
                cur = truck_weights[idx]
                bridge.append((cur, answer+bridge_length))
                w += cur
                idx += 1
            else:
                answer = bridge[0][1]
                continue
        answer += 1
        #print('{0} : {1}'.format(answer,bridge))
    return answer
