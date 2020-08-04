# 외벽 점검
# https://programmers.co.kr/learn/courses/30/lessons/60062

from itertools import permutations
from collections import deque

def solution(n, weak, dist):
    dist = sorted(dist, reverse = -1)
    # 친구 1명일때
    weak_test = deque(weak)
    for _ in range(len(weak)):
        d = dist[0]
        if weak_test[0] + d >= weak_test[-1]:
            return 1
        weak_test.rotate(-1)
        weak_test[-1] += n
        
    for ans in range(2,len(dist)+1):
        for candidate in permutations(dist[:ans]): # candidate: 선택된 친구들의 이동거리
            weak_test = deque(weak)
            for _ in range(len(weak)):
                testing, can = weak_test.copy(), deque(candidate)
                while can and testing:
                    start, d = testing.popleft(), can.popleft()
                    while testing and testing[0] <= start + d:
                        testing.popleft()
                if not testing:
                        return ans
                weak_test.rotate(-1)
                weak_test[-1] += n
    return -1