# https://www.acmicpc.net/problem/11724
# 연결 요소의 개수

from sys import stdin, setrecursionlimit
setrecursionlimit(100000000)
input = stdin.readline

def dfs(cur):
    visited[cur] = True
    for node, edge in enumerate(arr[cur]):
        if not visited[node] and edge:
            dfs(node)

if __name__ == "__main__":
    V, E = map(int, input().split())

    arr = [[False]*V for _ in range(V)]
    for _ in range(E):
        u,v = map(int, input().split())
        arr[u-1][v-1] = arr[v-1][u-1] = True

    visited = [False]*V
    answer = 0
    for v in range(V):
        if not visited[v]:
            dfs(v)
            answer += 1

    print(answer)

    