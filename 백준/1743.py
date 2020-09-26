# https://www.acmicpc.net/problem/1743
# 음식물 피하기
from collections import deque

N, M, K = map(int, input().split())
board = [[0]*M for _ in range(N)]
foods = deque()
for _ in range(K):
    r, c = map(int, input().split())
    foods.append((r-1,c-1))
    board[r-1][c-1] = 1

answer = 0
dr, dc = (1,-1,0,0), (0,0,-1,1)
for pos in foods:
    r, c = pos[0], pos[1]
    cnt = 1
    board[r][c] = 0
    queue = deque()
    queue.append((r,c))
    while queue:
        curr, curc = queue.popleft()
        for i in range(4):
            nr, nc = curr+dr[i], curc+dc[i]
            if nr<0 or nr>=N or nc<0 or nc>=M:
                continue
            if board[nr][nc] == 1:
                cnt += 1
                board[nr][nc] = 0
                queue.append((nr,nc))
    answer = max(cnt, answer)

print(answer)