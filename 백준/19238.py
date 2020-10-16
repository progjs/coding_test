# https://www.acmicpc.net/problem/19238
# 스타트 택시 

from collections import deque

dr, dc = (-1,0,0,1), (0,-1,1,0)

def bfs1(curr, curc):
    visited = [[False]*N for _ in range(N)]
    q = deque()
    q.append([curr, curc])
    visited[curr][curc] = True
    dist = 0 # 거리 = 연료 사용량
    
    while True:
        cust = []
        dist += 1
        if dist >= fuel: # 연료 부족
            return None
        qsize = len(q) # 거리 같은 지점들만 탐색하기 위해
        for _ in range(qsize): # 탐색
            r,c = q.popleft()
            for i in range(4): # 상하좌우 탐색
                nr, nc = r+dr[i], c+dc[i]
                if nr<0 or nr>=N or nc<0 or nc>=N:
                    continue
                if visited[nr][nc] or arr[nr][nc] == 1:
                    continue
                if arr[nr][nc] > 1: # 승객 있으면
                    cust.append([nr, nc])
                q.append([nr, nc])
                visited[nr][nc] = True
        if cust: # 현재 거리 dist에서 승객이 있으면 그만 탐색
            break
    else: # 갈 수 있는 승객이 없으면
        return None
    
    if len(cust) > 1: # 거리 같은 승객 여러명이면
        cust.sort()
    return cust[0][0], cust[0][1], dist


def bfs2(curr, curc, endr, endc):
    dist = [[-1]*N for _ in range(N)]
    q = deque()
    q.append([curr, curc])
    dist[curr][curc] = 0   

    while q:
        r,c = q.popleft()
        if dist[r][c] >= fuel: # 연료 부족
            return None
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if nr<0 or nr>=N or nc<0 or nc>=N:
                continue
            if dist[nr][nc] != -1 or arr[nr][nc] == 1:
                continue
            if nr == endr and nc == endc: # 승객목적지 도착
                return dist[r][c] + 1
            q.append([nr, nc])
            dist[nr][nc] = dist[r][c] + 1
    

if __name__=="__main__":
    N, M, fuel = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    goals = []
    tr, tc = list(map(int, input().split())) # 택시위치
    for i in range(M):
        r,c,pr,pc = map(int, input().split())
        arr[r-1][c-1] = i+2 # 1: 벽, 2~: 승객
        goals.append([pr-1, pc-1]) # 승객 목적지
    tr, tc = tr-1, tc-1

    cust_num = M
    while cust_num > 0:
        if arr[tr][tc] > 1: # 택시위치에 승객이 있으면
            gr, gc = goals[arr[tr][tc]-2]
            d = bfs2(tr, tc, gr, gc)
            if d is None: # 목적지에 갈 수 없으면
                print(-1)
                break
            fuel += d # 연료 충전
            arr[tr][tc] = 0 # 승객 삭제
            cust_num -= 1
            tr, tc = gr, gc
        else:
            tmp = bfs1(tr, tc)
            if tmp is None:
                print(-1)
                break
            nr, nc, d = tmp # 승객위치, 거리
            fuel -= d # 연료 소진
            tr, tc = nr, nc # 택시를 승객위치로 이동
    else:
        print(fuel)