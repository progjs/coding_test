# https://www.acmicpc.net/problem/2606
# 바이러스

from collections import deque

V = int(input())
E = int(input())

arr = [[0]*V for _ in range(V)]
for _ in range(E):
    u,v = map(int, input().split())
    arr[u-1][v-1] = arr[v-1][u-1] = 1

visited = [False]*V
queue = deque([0])
visited[0] = True

answer = 0
while queue:
    cur = queue.popleft()
    for i, e in enumerate(arr[cur]):
        if e == 1 and not visited[i]:
            queue.append(i)
            visited[i] = True
            answer += 1

print(answer)
