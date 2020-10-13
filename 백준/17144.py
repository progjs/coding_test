# https://www.acmicpc.net/problem/17144
# 미세먼지 안녕!

dr, dc = (0,0,-1,1), (1,-1,0,0)

def spread():
    global R, C, rec, board, board2
    board2 = [[0]*C for _ in range(R)] # 미세먼지 확산 후 저장
    
    for r in range(R):
        for c in range(C):
            cnt, dust = 0, board[r][c]//5
            if board[r][c] >= 5: # 미세먼지 확산 가능
                for i in range(4): # 상하좌우
                    nr, nc = r+dr[i], c+dc[i]
                    if 0<=nr<R and 0<=nc<C and board[nr][nc] != -1:
                        cnt += 1
                        board2[nr][nc] += dust
            board2[r][c] = board2[r][c] + board[r][c] - cnt*dust

    # 회전- 반시계
    for i in range(rec[0]-2, -1, -1):
        board2[i+1][0] = board2[i][0]
    for i in range(1, C):
        board2[0][i-1] = board2[0][i]
    for i in range(1, rec[0]+1):
        board2[i-1][-1] = board2[i][-1]
    for i in range(C-2, 0, -1):
        board2[rec[0]][i+1] = board2[rec[0]][i]
    board2[rec[0]][1] = 0 # 공기청정기 출발점 옆 = 0
    
    # 회전 - 시계
    for i in range(rec[1]+2, R):
        board2[i-1][0] = board2[i][0]
    for i in range(1, C):
        board2[-1][i-1] = board2[-1][i]
    for i in range(R-2, rec[1]-1, -1):
        board2[i+1][-1] = board2[i][-1]
    for i in range(C-2, 0, -1):
        board2[rec[1]][i+1] = board2[rec[1]][i]
    board2[rec[1]][1] = 0


if __name__ == "__main__":
    R, C, T = map(int, input().split())
    rec, board = [], [] # 공기청정기 위치, 미세먼지 지도
    for i in range(R):
        board.append(list(map(int, input().split())))
        if board[-1][0] == -1:
            rec.append(i)

    board2 = [[0]*C for _ in range(R)]
    for t in range(T):
        spread()
        board = board2.copy() # 초기화

    board[rec[0]][0] = 0
    board[rec[1]][0] = 0
    total = 0 # 미세먼지 총합
    for i in range(R):
        for j in range(C):
            total += board[i][j]
    print(total) # 공기청정기 값 제외
