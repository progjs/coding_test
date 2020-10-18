# 뱀
# https://www.acmicpc.net/problem/3190

from sys import stdin
from collections import deque
input = stdin.readline

dx = [0,0,-1,1] # 상하좌우
dy = [-1,1,0,0]

N = int(input())
K = int(input())
board = [[0]*(N+2) for _ in range(N+2)]
board[0] = [3]*(N+2)
board[N+1] = [3]*(N+2)
for i in range(1,N+2):
    board[i][0], board[i][N+1] = 3, 3

for _ in range(K): # 사과
    x,y = map(int, input().split())
    board[x][y] = 1

cnt = int(input())
turns = deque()
for _ in range(cnt):
    turns.append(tuple(input().split()))

change = {'D':[3,2,0,1], 'L':[2,3,1,0]}
t, dir = 0, 3
snake = deque([[1,1]])
board[1][1] = 2

# for i in range(N+2):
#     print(board[i])

while True:
    t += 1 # 1초 경과 (이 방향으로 몇초동안 이동했는지 계산하려고)
    # 뱀 머리 이동
    snake.appendleft([snake[0][0]+dx[dir], snake[0][1]+dy[dir]])
    s_head = snake[0]

    if board[s_head[1]][s_head[0]] == 1: # 사과있음
        board[s_head[1]][s_head[0]] = 2
    elif board[s_head[1]][s_head[0]] == 0: # 꼬리 삭제
        s_tail = snake.pop()
        board[s_tail[1]][s_tail[0]] = 0
        board[s_head[1]][s_head[0]] = 2
    else:
        break

    # print("{}초: {} {}".format(t, s_head, s_tail))
    # for i in range(N+2):
    #     print(board[i])

    # 방향 전환
    if turns and t == int(turns[0][0]): 
        # print("방향 바뀜")
        dir = change[turns.popleft()[1]][dir]
    
print(t)