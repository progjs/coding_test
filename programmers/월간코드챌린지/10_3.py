'''
입출력 예
n	edges	result
4	[[1,2],[2,3],[3,4]]	2
5	[[1,5],[2,5],[3,5],[4,5]]	2
'''

# 시간초과
# 다익스트라 알고리즘
# 한 정점에서 모든 정점으로의 최단거리를 구하는 알고리즘

# 모든 정점에 대해 다익스트라 알고리즘을 실행해서 각 정점간의 최소 거리를 찾고
# combinations으로 모든 정점 3개에 대해 중간값 중 최대값을 찾는다.

from itertools import combinations

arr = []

def search2(start, n):
    global arr
    d = [9876543210]*n
    for i, a in enumerate(arr[start]):
        if a != 0:
            d[i] = 1
    visit = [False]*n
    d[start], visit[start] = 0, True

    while True:
        min_node = [-1,9876543210]
        for i,value in enumerate(d): # 아직 방문안한 거리가 최소인 노드 찾기
            if not visit[i] and value <= min_node[1]:
                min_node = [i, value]

        if min_node[0] == -1: # 모두 방문했으면 종료
            return d

        visit[min_node[0]] = True
        for node in range(n):
            if not visit[node] and arr[min_node[0]][node]: # 방문 안했고, 간선이 존재하면
                if d[node] > d[min_node[0]] + 1: # 거리 최소값 update
                    d[node] = d[min_node[0]] + 1

def solution2(n, edges):
    global arr
    
    arr = [[0]*n for _ in range(n)]
    for e in edges:
        arr[e[0]-1][e[1]-1] = 1
        arr[e[1]-1][e[0]-1] = 1
        
    dist = []
    for i in range(n):
        dist.append(search2(i, n))
    
    answer = 0
    for case in combinations(range(n), 3):
        result = sorted([dist[case[0]][case[1]], dist[case[0]][case[2]], dist[case[1]][case[2]]])[1]
        if result > answer:
            answer = result
    return answer


# 시간초과
# Floyd 알고리즘
# 모든 정점에서 모든 정점으로의 최단거리를 구하는 알고리즘
from itertools import combinations
import sys

dist = []
INF = sys.maxsize

def search(n):
    global INF, dist
            
    for k in range(n): # 연결고리
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]    


def solution(n, edges):
    global INF, dist
    
    dist = [[INF]*n for _ in range(n)]
    for e in edges:
        dist[e[0]-1][e[1]-1] = 1
        dist[e[1]-1][e[0]-1] = 1
        
    search(n)
    
    answer = 0
    for case in combinations(range(n), 3):
        result = sorted([dist[case[0]][case[1]], dist[case[0]][case[2]], dist[case[1]][case[2]]])[1]
        if result > answer:
            answer = result
    return answer


if __name__ == "__main__":
    # 플로이드
    print(solution(4, [[1,2],[2,3],[3,4]])) # 2
    print(solution(5, [[1,5],[2,5],[3,5],[4,5]])) # 2

    # 다익스트라
    print(solution2(4, [[1,2],[2,3],[3,4]])) # 2
    print(solution2(5, [[1,5],[2,5],[3,5],[4,5]])) # 2
