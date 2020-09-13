# 로봇 청소기
# https://www.acmicpc.net/problem/14503

# 북동남서
# 0 1 2 3
dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]

def dfs(r, c, d):
    global N, M, answer, board
    
    for i in range(4):
        d = (d+3) % 4
        nr, nc = r+dr[d], c+dc[d]
        if 0 <= nr < N and 0 <= nc < M and board[nr][nc] == '0':
            board[nr][nc] = '2'
            answer += 1
            dfs(nr, nc, d)
            break
    else:
        nr, nc = r-dr[d], c-dc[d]
        if board[nr][nc] == '1':
            return
        dfs(nr, nc, d)
       
if __name__ == "__main__":
    N, M = map(int, input().split())
    r, c, d = map(int, input().split())
    board = []
    for _ in range(N): # 1: 벽
        board.append(list(input().split()))

    board[r][c] = '2'
    answer = 1
    dfs(r,c,d)
    print(answer)
