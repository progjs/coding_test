# https://www.acmicpc.net/problem/1753
# 최단경로

from sys import maxsize, stdin
from heapq import heappop, heappush

INF = maxsize
input = stdin.readline

def dijkstra(start, V):
    dist = [INF]*V
    dist[start] = 0

    heap = []
    heappush(heap, [0, start]) # [가중치, 정점]
    while heap:
        weight, node = heappop(heap) # k로부터의 거리가 최소인 정점
        for n, w in arr[node]: # 모든 간선에 대해
            total = w + weight
            if total < dist[n]: # node를 지나서 n으로 가는 거리의 최소값 갱신
                dist[n] = total
                heappush(heap, [total, n])
    return dist


if __name__ == "__main__":
    V,E = map(int, input().split())
    k = int(input()) - 1 # 시작정점

    arr = [[] for _ in range(V)]

    for _ in range(E):
        u,v,w = map(int, input().split())
        arr[u-1].append([v-1,w])

    for d in dijkstra(k,V):
        print(d if d != INF else 'INF')
        