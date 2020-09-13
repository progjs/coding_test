# 자물쇠와 열쇠
# https://programmers.co.kr/learn/courses/30/lessons/60059

N, M = 0,0

def rotate_key(board):
    n = len(board)
    result = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[j][n-1-i] = board[i][j]
    return result

def check(r, c, key, lock):
    global N, M
    board = [[0]*(N + 2*(M-1)) for _ in range((N + 2*(M-1)))]
    for i in range(M):
        for j in range(M):
            board[r+i][c+j] = key[i][j]
    
    for i in range(M-1, M-1+N):
        for j in range(M-1, M-1+N):
            board[i][j] += lock[i-M+1][j-M+1]
            if board[i][j] != 1:
                return False
    return True
            
def solution(key, lock):
    global N, M
    N, M = len(lock), len(key)
    
    for _ in range(4):
        for r in range(M-1+N):
            for c in range(M-1+N):
                if check(r,c,key,lock):
                    return True 
        key = rotate_key(key)
    return False