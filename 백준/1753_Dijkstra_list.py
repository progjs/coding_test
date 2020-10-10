# https://www.acmicpc.net/problem/1753
# 최단경로

from sys import maxsize

INF = maxsize

def dijkstra(k, v):
    visited = [False]*v
    visited[k] = True
    dist = arr[k] + [INF]

    for _ in range(v):
        node = -1
        for i,value in enumerate(visited): # 방문 안한 최소 노드 찾고
            if not value and dist[i] < dist[node]:
                node = i
        visited[node] = True

        for i in range(v): # k부터의 거리 update
            d = dist[node] + arr[node][i]
            if d < dist[i]:
                dist[i] = d   
    return dist[:-1]


if __name__ == "__main__":
    v,e = map(int, input().split())
    k = int(input()) - 1 # 시작정점

    arr = [[INF]*v for _ in range(v)]
    for i in range(v):
        arr[i][i] = 0

    for _ in range(e):
        u,v,w = map(int, input().split())
        arr[u-1][v-1] = min(w, arr[u-1][v-1])
        
    for d in dijkstra(k,v):
        print(d if d != INF else 'INF')