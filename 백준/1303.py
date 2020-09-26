# https://www.acmicpc.net/problem/1303
# 전쟁 - 전투
# BFS

from collections import deque

N, M = map(int, input().split())
board = []
for _ in range(M):
    board.append(list(input()))

ans = [0, 0]
colors = 'WB'
dr, dc = (1,-1,0,0), (0,0,-1,1)
for col in range(2):
    for i in range(M):
        for j in range(N):
            if board[i][j] == colors[col]:
                cnt, queue = 1, deque()
                board[i][j] = '0'
                queue.append([i,j])
                while queue:
                    cr, cc = queue.popleft()
                    for t in range(4):
                        nr, nc = cr+dr[t], cc+dc[t]
                        if nr<0 or nr>=M or nc<0 or nc>=N:
                            continue
                        if board[nr][nc] == colors[col]:
                            queue.append([nr, nc])
                            board[nr][nc] = '0'
                            cnt += 1
                ans[col] += cnt**2
print(ans[0], ans[1])