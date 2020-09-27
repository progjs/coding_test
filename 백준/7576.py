# https://www.acmicpc.net/problem/7576
# 토마토

from collections import deque

M, N = map(int, input().split()) #col row
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

def bfs():
    global M, N, board
    queue = deque()

    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                queue.append((i,j))

    dr, dc = (1,-1,0,0), (0,0,-1,1)
    while queue:
        r,c = queue.popleft()
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if nr<0 or nr>=N or nc<0 or nc>=M:
                continue
            if board[nr][nc] == 0:
                queue.append((nr, nc))
                board[nr][nc] = board[r][c] + 1

    answer = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                return -1
            elif board[i][j] > answer:
                answer = board[i][j]
    return answer-1

print(bfs())


