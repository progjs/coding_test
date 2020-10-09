# https://www.acmicpc.net/problem/19238
# 스타트 택시

# dict.get(key, default)
from collections import deque

dr, dc = (-1,1,0,0), (0,0,-1,1)

def bfs(start, end):
    visited = [[-1]*(N+1) for _ in range(N+1)]
    queue = deque()
    queue.append(start)
    visited[start[0]][start[1]] = 0
    while queue:
        r,c = queue.popleft()
        if [r,c] == end:
            return visited[r][c]

        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if nr<=0 or nr>N or nc<=0 or nc>N:
                continue
            if not board[nr][nc] and visited[nr][nc] == -1:
                visited[nr][nc] = visited[r][c]+1
                queue.append([nr, nc])
    return -1 # 승객->목적지 이동 실패


def select_p(car):
    visited = [[-1]*(N+1) for _ in range(N+1)]
    queue = deque()
    queue.append(car)
    visited[car[0]][car[1]] = 0
    while queue:
        rot = len(queue)
        candidates = []
        for _ in range(rot):
            r,c = queue.popleft()
            for i in range(4):
                nr, nc = r+dr[i], c+dc[i]
                if nr<=0 or nr>N or nc<=0 or nc>N:
                    continue
                if board[nr][nc] != 1 and visited[nr][nc] == -1:
                    visited[nr][nc] = visited[r][c] + 1
                    queue.append([nr, nc])
                    if board[nr][nc] > 1:
                        candidates.append([nr, nc, visited[nr][nc]])
        if candidates:
            s = sorted(candidates)[0]
            return [board[s[0]][s[1]], s[-1]]
    return [-1,-1] # 실패


if __name__ == "__main__":
    N, M, power = map(int, input().split())
    board = [[0]*(N+1)]
    for _ in range(N):
        board.append([0]+list(map(int, input().split())))
    car = list(map(int, input().split()))
    people = [list(map(int, input().split())) for _ in range(M)]
    # 승객위치, 목적지위치
    for i, p in enumerate(people):
        board[p[0]][p[1]] = i+2 # 승객

    for _ in range(M):
        if board[car[0]][car[1]] > 1: # 현재 택시 위치에 승객이 있다면
            person = people[board[car[0]][car[1]]-2]
        else:
            p_idx, p_dist = select_p(car) ### 선택한 승객 좌표, 거리
            if p_dist < 0 or power <= p_dist:
                print(-1)
                break
            power -= p_dist
            person = people[p_idx-2] 
        board[person[0]][person[1]] = 0
        dist_f = bfs(person[:2], person[2:]) # 승객->목적지 거리
        if dist_f < 0 or power <= dist_f: # 목적지 도달X or 연료부족
            print(-1)
            break
        power += dist_f # 연료 충전
        car = person[2:] # 택시 위치를 목적지로 변경
    else:
        print(power)