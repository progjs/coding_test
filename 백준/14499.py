# https://www.acmicpc.net/problem/14499
# 14499 주사위 굴리기

from sys import stdin
input = stdin.readline

def move(direction):
    global dice
    if direction == 1:
        dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]
    elif direction == 2:
        dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
    elif direction == 3:
        dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]
    elif direction == 4:
        dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]

N, M, x, y, K = map(int, input().split())
board = []
for i in range(N):
    board.append(list(map(int, input().split())))
directions = list(map(int, input().split()))

dice = [0] * 7
d = [0, (0,1), (0,-1), (-1,0), (1,0)]
for m in directions:
    dx, dy = d[m]
    if 0<= x+dx < N and 0 <= y+dy < M:
        x, y = x+dx, y+dy
        move(m)
        if board[x][y] == 0:
            board[x][y] = dice[1]
        else:
            dice[1] = board[x][y]
            board[x][y] = 0
        print(dice[6])
