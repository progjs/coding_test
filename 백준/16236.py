# https://www.acmicpc.net/problem/16236
# 아기 상어
'''
1. 상어 위치 저장
2. 먹을 수 있는 작은 물고기를 못찾을 때까지 while문 반복
2-1. bfs
    큐와 최소힙 사용
    - 방문 안한 곳이면 -> 방문 표시
        - 0 or 상어크기랑 물고기 크기 같으면 -> 큐에 (r,c,거리+1)추가
        - 물고기 크기 작으면 -> heap에 (거리, row, col) 추가
        - 물고기 크기가 크면(else) 패스
    return heap[0]로 먹을 물고기 도출
2-2. 먹을 수 있는 물고기가 없으면 break
    있으면 -> 먹은 물고기 개수 +1 & 시간+=거리 & 물고기 위치=0
              & 상어 위치 변경
2-3. 상어크기 == 먹은 물고기 개수 -> 상어크기+1 & 먹은 개수=0
3. 시간 출력
'''


from collections import deque
import heapq

dr, dc = (-1,1,0,0), (0,0,-1,1)

def bfs(ssr, ssc):
    visited = [[False]*N for _ in range(N)]
    hp = []
    queue = deque()
    queue.append([ssr, ssc, 0])
    visited[ssr][ssc] = True

    while queue:
        r, c, d = queue.popleft()

        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if nr<0 or nr>=N or nc<0 or nc>=N or visited[nr][nc] == True:
                continue
            visited[nr][nc] = True # 방문표시
            if sea[nr][nc] == 0 or sea[nr][nc] == size: # 물고기 없거나 크기 같은 물고기 있는지
                queue.append([nr, nc, d+1])
            elif sea[nr][nc] < size: # 작은 물고기 발견
                heapq.heappush(hp, [d+1, nr, nc]) # 우선순위: 거리, 위, 왼쪽
            # else: 상어보다 큰 물고기가 있는 곳은 지나갈 수 없다.
    if hp:
        return hp[0]
    return None


if __name__=="__main__":
    N = int(input())
    sea = [list(map(int, input().split())) for _ in range(N)]
    sr, sc = -1, -1

    for i in range(N):
        for j in range(N):
            if sea[i][j] == 9:
                sr, sc = i, j
    sea[sr][sc] = 0

    size, eat, t = 2, 0, 0
    while True:
        nxt = bfs(sr, sc)
        if nxt == None: # 잡아먹을 물고기가 없으면 엄마상어 호출
            break
        eat += 1
        t += nxt[0] # 상어-물고기 거리 = 시간
        sea[nxt[1]][nxt[2]] = 0
        sr, sc = nxt[1], nxt[2] # 상어위치 변경

        if eat == size:
            size += 1
            eat = 0

    print(t)