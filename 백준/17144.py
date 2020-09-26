R, C, T = map(int, input().split())
rec, board = [], []
for i in range(R):
    board.append(list(map(int, input().split())))
    if board[-1][0] == -1:
        rec.append(i)

dr, dc = (0,0,-1,1), (1,-1,0,0)
def spread():
    global R, C, rec, board, board2
    board2 = [[0]*C for _ in range(R)]
    
    for r in range(R):
        for c in range(C):
            cnt, dust = 0, board[r][c]//5
            if board[r][c] > 4:
                for i in range(4):
                    nr, nc = r+dr[i], c+dc[i]
                    if 0<=nr<R and 0<=nc<C and board[nr][nc] != -1:
                        cnt += 1
                        board2[nr][nc] += dust
            board2[r][c] = board2[r][c] + board[r][c] - cnt*board[r][c]
    
    for i in range(rec[0]-2, -1, -1):
        board2[i+1][0] = board2[i][0]
    for i in range(1,C):
        board2[0][i-1] = board2[0][i]
    for i in range(1, rec[0]+1):
        board2[i-1][-1] = board2[i][-1]
    for i in range(C-2, 0, -1):
        board2[rec[0]][i+1] = board2[rec[0]][i]
    board2[rec[0]][1] = 0

    for i in range(rec[1]+2, r):
        board2[i-1][0] = board2[i][0]
    for i in range(1,C):
        board2[-1][i-1] = board2[-1][i]
    for i in range(R-2, rec[1]-1, -1):
        board2[i+1][-1] = board2[i][-1]
    for i in range(C-2, 0, -1):
        board2[rec[1]][i+1] = board2[rec[1]][i]
    board2[rec[1]][1] = 0 


board2 = [[0]*C for _ in range(R)]
for t in range(T):
    spread()
    board = board2.copy()

total = 0
for i in range(R):
    for j in range(C):
        total += board[i][j]
print(total+2)
