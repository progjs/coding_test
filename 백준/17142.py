# 연구소3

from itertools import combinations
from collections import deque

dr, dc = (-1,1,0,0), (0,0,-1,1)

def spread(e):
    global N, arr, dist
    dist = [[-1]*N for _ in range(N)]
    queue = deque()
    for r,c in e:
        dist[r][c] = 0
        queue.append([r,c])

    time = 0
    while queue:
        r,c = queue.popleft()
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if nr<0 or nr>=N or nc<0 or nc>=N or dist[nr][nc] != -1:
                continue
            if arr[nr][nc] == 0 or arr[nr][nc] == 2:
                dist[nr][nc] = dist[r][c] +1
                queue.append([nr, nc])
                time = max(time, dist[nr][nc])
    a = list(sum(dist,[]))
    if a.count(-1) == list(sum(arr,[])).count(1):
        return time
    return None


if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = []
    virus = []
    for i in range(N):
        arr.append(list(map(int, input().split())))
        for j in range(N):
            if arr[-1][j] == 2:
                virus.append([i, j])

    answer = 987654321
    for e in combinations(virus, M):
        time = spread(e)
        if time is not None:
            answer = min(answer, time)

    print(answer)