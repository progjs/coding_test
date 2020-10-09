# ## 어른 상어
# n,m,k = map(int,input().split())
# array = [list(map(int, input().split())) for _ in range(n)]
# directions = list(map(int,input().split()))
# prio = [[] for _ in range(m)]
# for i in range(m):
#     for j in range(4):
#         prio[i].append(list(map(int,input().split())))
        
# smell = [[[0,0]]*n for _ in range(n)]
# dx=[-1,1,0,0]
# dy=[0,0,-1,1]

# def update_smell():
#     # 각 위치를 하나씩 확인하며
#     for i in range(n):
#         for j in range(n):
#             # 냄새가 존재하는 경우, 시간을 1만큼 감소시키기
#             if smell[i][j][1] > 0:
#                 smell[i][j][1] -= 1
#             # 상어가 존재하는 해당 위치의 냄새를 k로 설정
#             if array[i][j] != 0:
#                 smell[i][j] = [array[i][j], k]
    
# def move():
#     new_array = [[0]*n for _ in range(n)]
#     for x in range(n):
#         for y in range(n):
#             if array[x][y] != 0:
#                 direction = directions[array[x][y]-1]
#                 #상하좌우로 냄새가 없는곳이 있는지
#                 found = False
#                 for index in range(4):
#                     nx = x+dx[prio[array[x][y]-1][direction-1][index]-1]
#                     ny = y+dy[prio[array[x][y]-1][direction-1][index]-1]
#                     if 0<=nx and nx<n and 0<=ny and ny<n:
#                         if smell[nx][ny][1] == 0:  #냄새가 존재하지 않는곳이면
#                             directions[array[x][y]-1] = prio[array[x][y]-1][direction-1][index]
#                             if new_array[nx][ny] == 0:
#                                 new_array[nx][ny] = array[x][y]
#                             else:
#                                 new_array[nx][ny] = min(new_array[nx][ny],array[x][y])
#                             found=True
#                             break
#                 if found:
#                     continue
#                 for index in range(4):
#                     nx = x+dx[prio[array[x][y]-1][direction-1][index]-1]
#                     ny = y+dy[prio[array[x][y]-1][direction-1][index]-1]
#                     if 0<=nx and nx<n and 0<=ny and ny<n:
#                         if smell[nx][ny][0] == array[x][y]:
#                             directions[array[x][y]-1] = prio[array[x][y]-1][direction-1][index]
#                             new_array[nx][ny] = array[x][y]
#                             break
#     return new_array
    
     
# time = 0
# while True:
#     update_smell()
#     new_array = move() #모든 상어 이동시키기
#     array = new_array
#     time += 1
    
#     #1번 상어만 남았는지 체크
#     check=True
#     for i in range(n):
#         for j in range(n):
#             if array[i][j] > 1:
#                 check=False
                
#     if check:
#         print(time)
#         break
        
#     if time>=1000:
#         print(-1)
#         break

# --------------------------

# 스타트 택시
from collections import deque
import sys

input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs1(x, y): # cnt에 이동거리를 더하며 이동
    global fuel
    q1.append([x, y]) # 택시 현위치 추가
    c1[x][y], cnt = 1, 0 # 
    while q1:
        qlen = len(q1)
        p = []
        cnt += 1
        if cnt >= fuel: #fuel이 이동한 거리보다 작으면 0 반환
            return 0
        print(q1)
        for aaaa in c1:
            print(aaaa)
        for _ in range(qlen):
            x, y = q1.popleft()
            for i in range(4): # bfs
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < n: # 사이즈 제한
                    if a[nx][ny] != -1 and c1[nx][ny] == 0: # 벽이 아니고 방문하지 않았으면
                        if a[nx][ny] > 0: # 승객이 있으면
                            p.append([nx, ny]) # 승객의 좌표 저장
                        q1.append([nx, ny])
                        c1[nx][ny] = 1 
        if p: #탈 승객이 있으면
            break

    if not p: #탈 승객이 없으면 승객에게 이동할 수 없는 경우
        return 0

    fuel -= cnt # 사용한 fuel 제거
    p = sorted(p) # 정렬 승객 좌표는 p[0]
    x, y = p[0]
    res = bfs2(x, y, a[x][y])
    if res == 0:
        return 0
    
    length, nx, ny = res
    fuel += length
    a[x][y] = 0
    return nx, ny


def bfs2(x, y, idx): 
    q2.append([x, y]) # 택시 위치
    c2[x][y] = 0 # 택시로부터의 거리 저장 (택시위치니까 0으로 초기화)
    while q2:
        x, y = q2.popleft()
        if c2[x][y] >= fuel: # 연료 부족
            return 0 # 이동 불가능 0 return
        for i in range(4): 
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:#사이즈 제한
                if a[nx][ny] != -1 and c2[nx][ny] == -1: # a에서 -1은 벽 c2에서-1은 방문안함
                    q2.append([nx, ny])
                    c2[nx][ny] = c2[x][y] + 1 # 택시로부터의 거리 저장
                    if [nx, ny] == d[idx]: # 승객의 목적지
                        return c2[nx][ny], nx, ny # 택시이동거리, 목적지 좌표
    return 0


n, m, fuel = map(int, input().split())#
a = []#지도
for i in range(n):
    a.append(list(map(int, input().split())))
    for j in range(n):
        if a[i][j] == 1:
            a[i][j] = -1 # 벽을 -1로 표시

x, y = map(int, input().split())

d = [[] for _ in range(m+1)]
for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    a[x1-1][y1-1] = i+1 #승객번호
    d[i+1] = [x2-1, y2-1] #해당번호 승객 목적지

x -= 1; y -= 1
for _ in range(m):
    q1, c1 = deque(), [[0 for _ in range(n)] for _ in range(n)]
    q2, c2 = deque(), [[-1 for _ in range(n)] for _ in range(n)]

    if a[x][y] > 0: # 택시 위치에 승객이 있으면
        res = bfs2(x, y, a[x][y])
        if res == 0: # 택시가 목적지에 갈수 없으면
            print(-1)
            sys.exit()
        length, nx, ny = res # 택시이동거리, 목적지 좌표
        if length > fuel: # 연료 부족하면(중복되는 것 같다)
            print(-1)
            sys.exit()
        fuel += length # 연료 충전
        a[x][y] = 0 # 칸은 0으로 변경(승객 이동 완료)
        x, y = nx, ny # 현위치를 택시위치로 변경
        continue

    res = bfs1(x, y) # 현재 위치에 승객이 없으면 찾기
    if res == 0: # 안될 경우
        print(-1)
        sys.exit()
    else:
        x, y = res
print(fuel)