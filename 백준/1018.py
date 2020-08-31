# 체스판 다시 칠하기
# https://www.acmicpc.net/problem/1018

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(input())

for i in range(n):
    for j in range(m):
        print(board[i][j], end='')
    print()