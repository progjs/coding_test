# https://www.acmicpc.net/problem/15686
# 치킨 배달
'''
(2, 1)에 있는 집과 (1, 2)에 있는 치킨집과의 거리는 |2-1| + |1-2| = 2, (5, 5)에 있는 치킨집과의 거리는 |2-5| + |1-5| = 7이다. 따라서, (2, 1)에 있는 집의 치킨 거리는 2이다.

(5, 4)에 있는 집과 (1, 2)에 있는 치킨집과의 거리는 |5-1| + |4-2| = 6, (5, 5)에 있는 치킨집과의 거리는 |5-5| + |4-5| = 1이다. 따라서, (5, 4)에 있는 집의 치킨 거리는 1이다.
'''

'''
from collections import deque
dr, dc = [1,-1,0,0], [0,0,-1,1]

def bfs(cur, ch):
    d = [[-1]*N for _ in range(N)] # 거리
    for a,b in ch:
        d[a][b] = -2 # 치킨집

    queue = deque()
    queue.append(cur)
    d[cur[0]][cur[1]] = 0 # 집
    while queue:
        r,c = queue.popleft()
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0<=nr<N and 0<=nc<N:
                if d[nr][nc] == -1:
                    d[nr][nc] = d[r][c] + 1
                    queue.append([nr, nc])
                elif d[nr][nc] == -2: # 가장 가까운 치킨집 발견
                    return d[r][c] + 1
'''

from itertools import combinations

N, M = map(int, input().split()) # 도시크기, 폐업안한 치킨집 개수
city = [list(map(int, input().split())) for _ in range(N)]

houses, chickens = [], []
for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            chickens.append([i, j])
        elif city[i][j] == 1:
            houses.append([i, j])

answer = 9876543210
for e in combinations(list(range(len(chickens))), M):
    ch = [chickens[i] for i in e] # 폐업안한 치킨집
    total = 0
    for house in houses:
        min_dist = 9876543210
        for chicken in ch:
            min_dist = min(min_dist, abs(house[0]-chicken[0])+abs(house[1]-chicken[1]))
        total += min_dist
    answer = min(total, answer)

print(answer)
