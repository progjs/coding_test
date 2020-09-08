# 뱀
# https://www.acmicpc.net/problem/3190

from sys import stdin
from collections import deque
input = stdin.readline

dx = [0,0,-1,1] # 상하좌우
dy = [-1,1,0,0]

def find_tail(cur_x, cur_y, head):
    for i in range(4):
        new_x, new_y = cur_x+dx[i], cur_y+dy[i]
        if board[new_y][new_x] == 2:
            return [new_x, new_y]
    return head

N = int(input())
K = int(input())
board = [[0]*(N+2) for _ in range(N+2)]
board[0] = [3]*(N+2)
board[N+1] = [3]*(N+2)
for i in range(1,N+2):
    board[i][0], board[i][N+1] = 3, 3

for _ in range(K):
    x,y = map(int, input().split())
    board[x][y] = 1

cnt = int(input())
turns = deque()
for _ in range(cnt):
    turns.append(tuple(input().split()))

change = {'D':[3,2,0,1], 'L':[2,3,1,0]}
t, dir, s_head = 0, 3, [1,1]
s_tail = [1,1]
board[1][1] = 2
while True:
    t += 1 # 1초 경과
    # 뱀 머리 이동
    s_head[0] += dx[dir]
    s_head[1] += dy[dir]
    # print(s_head)

    if board[s_head[1]][s_head[0]] == 1:
        board[s_head[1]][s_head[0]] = 2
    elif board[s_head[1]][s_head[0]] == 0:
        board[s_head[1]][s_head[0]] = 2
        board[s_tail[1]][s_tail[0]] = 0
        s_tail = find_tail(s_tail[0], s_tail[1], s_head)
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