# 연구소
# https://www.acmicpc.net/problem/14502

from collections import deque
from sys import stdin
input = stdin.readline
dr = [1,-1,0,0]
dc = [0,0,1,-1]
N, M = 0, 0

def count_safty(after_board):
    ans = 0
    for i in range(N):
        for j in range(M):
            if after_board[i][j] == 0:
                ans += 1
    return ans


def bfs():
    global mx_ans, virus, board
    after_board = []
    for i in range(N):
        after_board.append([j for j in board[i]])
        
    queue = deque(virus)
    while queue:
        cur = queue.popleft()
        for i in range(4):
            nr, nc = cur[0]+dr[i], cur[1]+dc[i]
            if 0<=nr<N and 0<=nc<M and after_board[nr][nc] == 0:
                queue.append([nr, nc])
                after_board[nr][nc] = 2

    safe_size = count_safty(after_board)
    mx_ans = mx_ans if mx_ans > safe_size else safe_size


def select_wall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                board[i][j] = 1
                select_wall(cnt+1)
                board[i][j] = 0

# main
N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

virus = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 2:
            virus.append([i, j])

mx_ans = 0
select_wall(0)
print(mx_ans)

