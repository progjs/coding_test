# 뱀
# https://www.acmicpc.net/problem/3190

from sys import stdin
from collections import deque
input = stdin.readline

N = int(input())
K = int(input())
board = [[0]*(N+1) for _ in range(N+1)]
for _ in range(K):
    x,y = map(int, input().split())
    board[x][y] = 1

cnt = int(input())
turns = deque()
for _ in range(cnt):
    turns.append(tuple(input().split()))

print(turns)

t = 0
# while turns: