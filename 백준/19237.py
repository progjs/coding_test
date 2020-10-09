# https://www.acmicpc.net/problem/19237
# 어른 상어
from collections import deque

dr = (-1,1,0,0)
dc = (0,0,-1,1) # 상하좌우

N, M, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dirs = list(map(int, input().split()))

priority = {}
for i in range(M):
    p = [list(map(int, input().split())) for _ in range(4)]
    priority[i+1] = p

sharks = {}
visited = deque()
for i in range(N):
    for j in range(N):
        if board[i][j] == 0:
            continue
        sharks[board[i][j]] = [i, j, dirs[board[i][j]-1]]
        visited.append([i,j,k])
# print("----------입력값----------")
# for i, s in sharks.items():
#     print(i, s)
# for i,v in priority.items():
#     print(i, v)
# print("--------------------------")

t = 0
while t < 1000:
    if len(sharks.keys()) == 1:
        print(t)
        break
    t += 1

    deletes = [] # 제거할 상어 리스트
    for idx, shark in sharks.items():
        r,c,dir = shark
        # 상어 다음칸 찾기
        empty, same = [], []
        for d in priority[idx][dir-1]:
            nr, nc = r+dr[d-1], c+dc[d-1]
            if nr<0 or nr>=N or nc<0 or nc>=N:
                continue
            if board[nr][nc] == 0:
                empty.append([nr, nc, d])
            elif board[nr][nc] == idx:
                same.append([nr, nc, d])

        sharks[idx] = empty[0] if empty else same[0]
        # board에 새로운 칸 상어 표시
        # 다른 상어가 이미 있으면, 숫자 작은 상어만 남기고 sharks에서 삭제
        newr, newc, newd = sharks[idx]
        if board[newr][newc] != 0:
            if idx == board[newr][newc]:
                continue
            elif idx < board[newr][newc]:
                deletes.append(board[newr][newc])
                board[newr][newc] = idx
            else:
                deletes.append(idx)
        else:
            board[newr][newc] = idx

    # 겹친 상어들 삭제
    for s in deletes:
        del(sharks[s])

    # visited -1
    for v in visited:
        v[2] -= 1    
    # visited에서 0이면 삭제
    while visited:
        if visited[0][2] == 0:
            row, col, zero = visited.popleft()
            board[row][col] = 0
        else:
            break

    # 새로운 칸 visited에 추가
    for s in sharks.values():
        visited.append([s[0], s[1], k])
    
else:
    print(-1)
