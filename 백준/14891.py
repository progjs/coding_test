# https://www.acmicpc.net/problem/14891
# 톱니바퀴

from collections import deque

gears = [deque(list(input())) for _ in range(4)]
k = int(input())
rotation = [tuple(map(int, input().split())) for _ in range(k)]

for g, d in rotation:
    dirs = [0,0,0,0]
    dirs[g-1] = d
    cur = g-1
    while cur > 0: # 왼쪽
        if gears[cur-1][2] != gears[cur][6]:
            dirs[cur-1] = -dirs[cur]
        cur -= 1
    cur = g-1
    while cur < 3: # 오른쪽
        if gears[cur+1][6] != gears[cur][2]:
            dirs[cur+1] = -dirs[cur]
        cur += 1
    # 회전
    for i, d in enumerate(dirs):
        if d != 0:
            gears[i].rotate(d)

# 점수 계산    
answer, score = 0, 1
for gear in gears:
    if gear[0] == '1':
        answer += score
    score *= 2

print(answer)